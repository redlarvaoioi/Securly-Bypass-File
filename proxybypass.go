package main

import (
	"io"
	"log"
	"net/http"
	"net/url"
	"strings"
)

func main() {
	http.HandleFunc("/", handleProxy)
	log.Println("Starting proxy server on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleProxy(w http.ResponseWriter, r *http.Request) {
	targetURL := r.URL.Query().Get("url")
	if targetURL == "" {
		http.Error(w, "URL parameter is missing", http.StatusBadRequest)
		return
	}

	parsedURL, err := url.Parse(targetURL)
	if err != nil {
		http.Error(w, "Invalid URL parameter", http.StatusBadRequest)
		return
	}

	proxyRequest, err := http.NewRequest(r.Method, parsedURL.String(), r.Body)
	if err != nil {
		http.Error(w, "Failed to create request", http.StatusInternalServerError)
		return
	}

	proxyRequest.Header = r.Header.Clone()
	client := &http.Client{}
	response, err := client.Do(proxyRequest)
	if err != nil {
		http.Error(w, "Failed to fetch URL", http.StatusInternalServerError)
		return
	}
	defer response.Body.Close()

	for k, v := range response.Header {
		for _, vv := range v {
			w.Header().Add(k, vv)
		}
	}

	if response.Header.Get("Content-Type") == "text/html" {
		bodyBytes, err := io.ReadAll(response.Body)
		if err != nil {
			http.Error(w, "Failed to read response body", http.StatusInternalServerError)
			return
		}

		bodyString := string(bodyBytes)
		replacedBody := strings.ReplaceAll(bodyString, `href="`, `href="/?url=`)
		replacedBody = strings.ReplaceAll(replacedBody, `src="`, `src="/?url=`)
		replacedBody = strings.ReplaceAll(replacedBody, `action="`, `action="/?url=`)
		w.Write([]byte(replacedBody))
	} else {
		w.WriteHeader(response.StatusCode)
		io.Copy(w, response.Body)
	}
}
