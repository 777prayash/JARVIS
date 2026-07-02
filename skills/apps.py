import os

from core.app_manager import (
    remember_app,
    open_app,
    remove_app,
)

from core.speech import speak


APPS = {
    "chrome": "start chrome",
    "notepad": "start notepad",
    "calculator": "start calc",
    "paint": "start mspaint",
    "command prompt": "start cmd"
}

CLOSE_APPS = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": ["CalculatorApp.exe", "calc.exe"],
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe"
}


def execute(command):

    command = command.lower().strip()

    # Remember App
    if command.startswith("remember "):

        app = command.replace("remember", "").strip()

        speak(f"Please select {app}")

        if remember_app(app):
            speak(f"{app} has been remembered.")
        else:
            speak("No application selected.")

        return True

    # Forget App
    if command.startswith("forget "):

        app = command.replace("forget", "").strip()

        if remove_app(app):
            speak(f"{app} removed from memory.")
        else:
            speak("I don't remember that application.")

        return True

    # Open App
    if command.startswith("open "):

        app = command.replace("open", "").strip()

        if open_app(app):
            speak(f"Opening {app}")
            return True

        if app in APPS:
            speak(f"Opening {app}")
            os.system(APPS[app])
            return True
        
        # Close App
    if command.startswith("close "):

        app = command.replace("close", "").strip()

        if app in CLOSE_APPS:

            speak(f"Closing {app}")

            process = CLOSE_APPS[app]

            if isinstance(process, list):
                for p in process:
                    os.system(f"taskkill /f /im {p}")
            else:
                os.system(f"taskkill /f /im {process}")

            return True

    return False