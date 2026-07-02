from core.auto_scan import scan_pc
from core.media import play_movie
import os
import webbrowser
import pyautogui

from core.folder_manager import (
    remember_folder,
    remove_folder,
    get_folder
)

from core.app_manager import (
    remember_app,
    open_app,
    remove_app,
    get_app_path
)
from core.speech import speak

# ===========================
# WEBSITES
# ===========================

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "whatsapp": "https://web.whatsapp.com",
    "instagram": "https://instagram.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
    "reddit": "https://reddit.com",
    "spotify": "https://open.spotify.com",
    "amazon": "https://amazon.in",
    "flipkart": "https://flipkart.com",
    "netflix": "https://netflix.com",
    "x": "https://x.com"
    "claude": "https://claude.ai",
    "perplexity": "https://www.perplexity.ai",
    "gemini": "https://gemini.google.com",
    "canva": "https://www.canva.com",
    "leetcode": "https://leetcode.com",
    "huggingface": "https://huggingface.co",
}

# ===========================
# WINDOWS APPS
# ===========================

APPS = {
    "chrome": "start chrome",
    "notepad": "start notepad",
    "calculator": "start calc",
    "paint": "start mspaint",
    "command prompt": "start cmd"
}

# ===========================
# CLOSE APPS
# ===========================

CLOSE_APPS = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": ["CalculatorApp.exe", "calc.exe"],
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe"
}


def execute(command):

    command = command.lower().strip()

    # ===========================
    # AUTO SCAN
    # ===========================

    if (
    "scan my pc" in command
    or "scan computer" in command
    or "initialize" in command
    or "initialize jarvis" in command
    or "system scan" in command
    or "scan everything" in command
    ):

        speak("Scanning your computer. This may take a few moments.")

        apps = scan_pc()

        if apps:
            speak(f"Scan completed. I found {len(apps)} applications.")
        else:
            speak("I couldn't find any supported applications.")

        return True

    # REMEMBER FOLDER
    # ===========================

    if command.startswith("remember my ") and " folder" in command:

        folder = (
            command.replace("remember my", "")
            .replace("folder", "")
            .strip()
        )

        speak(f"Please select your {folder} folder.")

        if remember_folder(folder):
            speak(f"I will remember your {folder} folder.")
        else:
            speak("No folder selected.")

        return True

   
    # ===========================
    # FORGET FOLDER
    # ===========================

    if command.startswith("forget my ") and " folder" in command:

        folder = (
            command.replace("forget my", "")
            .replace("folder", "")
            .strip()
        )

        if remove_folder(folder):
            speak(f"I forgot your {folder} folder.")
        else:
            speak("I don't remember that folder.")

        return True

    
    # ===========================
    # CLOSE WEBSITE TAB
    # ===========================

    if command.startswith("close "):

        name = command.replace("close", "").strip()

        if name in WEBSITES:
            speak(f"Closing {name}")
            pyautogui.hotkey("ctrl", "w")
            return True

        if name in CLOSE_APPS:

            speak(f"Closing {name}")

            process = CLOSE_APPS[name]

            if isinstance(process, list):

                for p in process:
                    os.system(f"taskkill /f /im {p}")

            else:
                os.system(f"taskkill /f /im {process}")

            return True

    # ===========================
    # PLAY SONG
    # ===========================

    # ===========================
    # PLAY MOVIE OR YOUTUBE
    # ===========================

    if command.startswith("play "):

        media = (
            command.replace("play", "")
            .replace("on vlc", "")
            .replace("on youtube", "")
            .replace("youtube", "")
            .strip()
        )

        # Play locally using VLC
        if "on vlc" in command:

            vlc_path = get_app_path("vlc")

            if not vlc_path:
                speak("Please remember VLC first.")
                return True

            folders = []

            for key in ["movies", "music", "anime", "series"]:

                folder = get_folder(key)

                if folder:
                    folders.append(folder)

            if play_movie(media, vlc_path, folders):
                speak(f"Playing {media}")
            else:
                speak(f"I could not find {media}.")

            return True

        # Otherwise search YouTube
        speak(f"Searching YouTube for {media}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={media}"
        )

        return True

    # ===========================
    # TAKE SCREENSHOT
    # ===========================

    if "take screenshot" in command:

        image = pyautogui.screenshot()

        image.save("screenshot.png")

        speak("Screenshot saved")

        return True

    # ===========================
    # RESTART COMPUTER
    # ===========================

    if "restart computer" in command:

        speak("Restarting your computer in five seconds.")

        os.system("shutdown /r /t 5")

        return True

    # ===========================
    # SHUTDOWN COMPUTER
    # ===========================

    if "shutdown computer" in command:

        speak("Shutting down your computer in five seconds.")

        os.system("shutdown /s /t 5")

        return True

    # ===========================
    # CANCEL SHUTDOWN
    # ===========================

    if "cancel shutdown" in command:

        os.system("shutdown /a")

        speak("Shutdown cancelled.")

        return True

    # ===========================
    # LOCK COMPUTER
    # ===========================

    if "lock computer" in command:

        speak("Locking your computer.")

        os.system("rundll32.exe user32.dll,LockWorkStation")

        return True

    return False