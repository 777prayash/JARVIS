def understand(command):

    command = command.lower()

    intents = {

        "open_chrome": [
            "open chrome",
            "launch chrome",
            "start chrome",
            "chrome",
            "open browser",
            "browser"
        ],

        "open_notepad": [
            "open notepad",
            "start notepad",
            "launch notepad"
        ],

        "shutdown": [
            "shutdown",
            "shutdown computer",
            "turn off computer",
            "power off",
            "switch off pc"
        ],

        "restart": [
            "restart",
            "restart computer",
            "reboot",
            "reboot computer"
        ],

        "hello": [
            "hello",
            "hi",
            "hey jarvis",
            "good morning",
            "good evening"
        ]
    }

    for intent, phrases in intents.items():

        for phrase in phrases:

            if phrase in command:
                return intent

    return None