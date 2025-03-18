# Securly-Bypass-File
A simple file extension called .securlybypass that can be opened in any GitHub Codespace. (meant for securly bypasses, DUH)

# How to use for dummies
create a codespace in this repo
then, in the terminal run 
```
chmod +x run.sh
```
Then, run 
```
./run.sh
```
This will run the .securlybypass file. 

# Later Updates
1. i might make this so that it works on the computer, that way you wont need to make a codespace everytime.
2. add a proxy using pyhton to the file to attempt to make it kind of undetectable

# Things To note

the launcher i made is very ugly, i didnt really have to much time to work on it, updates would be appreciated!!!



also u can use the GO proxy to bypass securly, any link works, have fun!!!!!!!

also please leave a star ; u see, its good for ego LOL

# Official guide for the proxy plx read

1. Open the terminal (codespace needed). Then, enter the following code:

   ```
   wget https://golang.org/dl/go1.20.linux-amd64.tar.gz
   ```
Wait until its done downloading.

2. After this, run the following code

   ```
   sudo tar -C /usr/local -xvzf go1.20.linux-amd64.tar.gz
   ```
This will extract GO so you can run commands to actually use the proxy.

3. No, add go to your $PATH

   ```
   export PATH=$PATH:/usr/local/go/bin
   ```

4. Then, reload the shell profile.

```
source ~/.bashrc
```
5. Run the following

   ```
   go run proxybypass.go
   ```
# Now, you should see (in the bottom right corner) something like ....Port 8000.. 
# Click on the ports tab. You should then see a port. Open it in your browser. It should say  "URL" parameter not found (or something like that)
# At the end of the URL (in the search bar) add /?url=   Next, after the equal sign, put any URL you want, but it must begin with https://
# Hit enter and watch the magic happen!
 


