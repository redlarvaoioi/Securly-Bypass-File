import os
import json
import platform

def disable_firefox_extensions():
    print("Disabling Firefox extensions...")
    firefox_profiles_path = os.path.expanduser('~/.mozilla/firefox')
    if not os.path.exists(firefox_profiles_path):
        print("Firefox profiles directory not found.")
        return

    for profile in os.listdir(firefox_profiles_path):
        if profile.endswith('.default-release') or profile.endswith('.default'):
            extensions_file_path = os.path.join(firefox_profiles_path, profile, 'extensions.json')
            if os.path.exists(extensions_file_path):
                with open(extensions_file_path, 'r+') as file:
                    data = json.load(file)
                    for addon in data.get('addons', []):
                        addon['active'] = False
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                print(f"Extensions disabled in profile: {profile}")
            else:
                print(f"No extensions file found in profile: {profile}")

def disable_edge_extensions():
    print("Disabling Microsoft Edge extensions...")
    if platform.system() == 'Windows':
        edge_profiles_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge', 'User Data')
        if not os.path.exists(edge_profiles_path):
            print("Edge profiles directory not found.")
            return

        for profile in os.listdir(edge_profiles_path):
            if profile.startswith('Profile'):
                preferences_file_path = os.path.join(edge_profiles_path, profile, 'Preferences')
                if os.path.exists(preferences_file_path):
                    with open(preferences_file_path, 'r+') as file:
                        data = json.load(file)
                        if 'extensions' in data:
                            data['extensions']['settings'] = {}
                        file.seek(0)
                        json.dump(data, file, indent=4)
                        file.truncate()
                    print(f"Extensions disabled in profile: {profile}")
                else:
                    print(f"No preferences file found in profile: {profile}")
    else:
        print("Microsoft Edge extension disabling is only supported on Windows.")

def disable_chrome_extensions():
    print("Disabling Chrome extensions...")
    chrome_profiles_path = ''

    if platform.system() == 'Windows':
        chrome_profiles_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data')
    elif platform.system() == 'Darwin':
        chrome_profiles_path = os.path.expanduser('~/Library/Application Support/Google/Chrome')
    elif platform.system() == 'Linux':
        chrome_profiles_path = os.path.expanduser('~/.config/google-chrome')
    elif platform.system() == 'Chrome OS':
        chrome_profiles_path = os.path.expanduser('~/.config/google-chrome')

    if not os.path.exists(chrome_profiles_path):
        print("Chrome profiles directory not found.")
        return

    for profile in os.listdir(chrome_profiles_path):
        if profile.startswith('Profile') or profile == 'Default':
            preferences_file_path = os.path.join(chrome_profiles_path, profile, 'Preferences')
            if os.path.exists(preferences_file_path):
                with open(preferences_file_path, 'r+') as file:
                    data = json.load(file)
                    if 'extensions' in data:
                        data['extensions']['settings'] = {}
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                print(f"Extensions disabled in profile: {profile}")
            else:
                print(f"No preferences file found in profile: {profile}")

def main():
    disable_firefox_extensions()
    disable_edge_extensions()
    disable_chrome_extensions()

if __name__ == "__main__":
    main()
