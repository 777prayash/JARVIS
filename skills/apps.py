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

    return False