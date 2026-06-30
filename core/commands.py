import os
import webbrowser
import pyautogui

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
    # OPEN WEBSITE
    # ===========================

    if command.startswith("open "):

        name = command.replace("open", "").strip()

        if name in WEBSITES:
            speak(f"Opening {name}")
            webbrowser.open(WEBSITES[name])
            return True

        if name in APPS:
            speak(f"Opening {name}")
            os.system(APPS[name])
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
    # GOOGLE SEARCH
    # ===========================

    if command.startswith("search google for"):

        query = command.replace(
            "search google for", ""
        ).strip()

        speak(f"Searching Google for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return True

    # ===========================
    # YOUTUBE SEARCH
    # ===========================

    if command.startswith("search youtube for"):

        query = command.replace(
            "search youtube for", ""
        ).strip()

        speak(f"Searching YouTube for {query}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

        return True

    # ===========================
    # PLAY SONG
    # ===========================

    if command.startswith("play"):

        song = (
            command.replace("play", "")
            .replace("on youtube", "")
            .replace("youtube", "")
            .strip()
        )

        speak(f"Searching YouTube for {song}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
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