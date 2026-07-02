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
    "photoshop": "photoshop.exe",
    "code": "code.exe",
    "python": "python.exe",
    "git": "git.exe",
    "telegram": "telegram.exe",
    "blender": "blender.exe",
    "epic games": "epicgameslauncher.exe",
    "riot client": "riotclientservices.exe",
    "battle.net": "battle.net.exe",
    "notepad++": "notepad++.exe"
}


def scan_pc():

    folders = [

        r"C:\Program Files",

        r"C:\Program Files (x86)",

        os.path.join(
            os.environ.get("LOCALAPPDATA", ""),
            "Programs"
        ),

        os.path.join(
            os.environ.get("APPDATA", ""),
            r"Microsoft\Windows\Start Menu\Programs"
        ),

        os.path.join(
            os.environ.get("USERPROFILE", ""),
            "Desktop"
        )
    ]

    apps = {}

    print("\n========== NOVA SCAN ==========\n")

    for folder in folders:

        if not os.path.exists(folder):
            continue

        print(f"Scanning: {folder}")

        for root, dirs, files in os.walk(folder):

            for file in files:

                for app, exe in KNOWN_APPS.items():

                    if file.lower() == exe.lower():

                        path = os.path.join(root, file)

                        apps[app] = path

                        print(f"Found: {app}")

    with open(APP_FILE, "w") as f:
        json.dump(apps, f, indent=4)

    print("\n========== SCAN COMPLETE ==========\n")

    return apps