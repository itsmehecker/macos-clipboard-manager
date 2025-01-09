import json
import os
import subprocess
import sys

CONFIG_FILE = 'config.json'

def install_dependencies():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def add_to_startup():
    plist_content = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.yourusername.clipboardmanager</string>
        <key>ProgramArguments</key>
        <array>
            <string>{os.path.join(os.getcwd(), 'start.sh')}</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>KeepAlive</key>
        <true/>
    </dict>
    </plist>
    """
    plist_path = os.path.expanduser('~/Library/LaunchAgents/com.yourusername.clipboardmanager.plist')
    with open(plist_path, 'w') as plist_file:
        plist_file.write(plist_content)
    subprocess.call(['launchctl', 'load', plist_path])

def main():
    current_directory = os.getcwd()

    if not os.path.exists(CONFIG_FILE):
        config = {"first_run": True, "workingdirectory": current_directory}
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)

    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)

    # Update the working directory to the current directory
    config["workingdirectory"] = current_directory

    if config.get("first_run"):
        print("Running for the first time. Installing dependencies...")
        install_dependencies()
        add_to_startup()
        config["first_run"] = False

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

    os.chdir(config.get("workingdirectory"))

if __name__ == "__main__":
    main()