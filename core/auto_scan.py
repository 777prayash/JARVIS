import os
import json

APP_FILE = "memory/apps.json"

KNOWN_APPS = {
    "chrome": "chrome.exe",
    "vlc": "vlc.exe",
    "steam": "steam.exe",
    "discord": "discord.exe",
    "spotify": "spotify.exe",
    "obs": "obs64.exe",
    "photoshop": "Photoshop.exe",
    "code": "Code.exe"
}


def scan_pc():

    folders = [
        r"C:\Program Files",
        r"C:\Program Files (x86)"
    ]

    apps = {}

    for folder in folders:

        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):

            for file in files:

                for app, exe in KNOWN_APPS.items():

                    if file.lower() == exe.lower():

                        apps[app] = os.path.join(root, file)

    with open(APP_FILE, "w") as f:
        json.dump(apps, f, indent=4)

    return apps