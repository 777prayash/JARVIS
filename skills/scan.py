from core.auto_scan import scan_pc
from core.speech import speak


def execute(command):

    command = command.lower()

    if (
        "scan my pc" in command
        or "scan computer" in command
        or "initialize" in command
        or "system scan" in command
    ):

        speak("Scanning your computer. Please wait.")

        apps = scan_pc()

        if apps:
            speak(f"Scan completed. I found {len(apps)} applications.")
        else:
            speak("I couldn't find any supported applications.")

        return True

    return False