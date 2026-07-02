import webbrowser

from core.profile_manager import load_profile
from core.app_manager import open_app
from core.speech import speak

WEBSITES = {
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "google": "https://google.com",
    "youtube": "https://youtube.com"
}


def execute(command):

    command = command.lower().strip()

    if not command.startswith("start "):
        return False

    profile = command.replace("start", "").strip()

    data = load_profile(profile)

    if not data:
        return False

    speak(f"Starting {profile} profile.")

    # Open apps
    for app in data.get("apps", []):

        if open_app(app):
            print(f"Opened app: {app}")
        else:
            print(f"Could not open app: {app}")

    # Open websites
    for site in data.get("websites", []):

        if site in WEBSITES:
            webbrowser.open(WEBSITES[site])

    return True