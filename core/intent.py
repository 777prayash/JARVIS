class Intent:

    OPEN = "open"
    CLOSE = "close"
    PLAY = "play"
    SEARCH = "search"
    REMEMBER = "remember"
    FORGET = "forget"
    SCAN = "scan"
    SYSTEM = "system"
    UNKNOWN = "unknown"


OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run"
]

CLOSE_WORDS = [
    "close",
    "exit",
    "quit",
    "stop"
]

PLAY_WORDS = [
    "play",
    "watch",
    "listen"
]

SEARCH_WORDS = [
    "search",
    "find",
    "look up"
]

REMEMBER_WORDS = [
    "remember",
    "save"
]

FORGET_WORDS = [
    "forget",
    "delete",
    "remove"
]

SCAN_WORDS = [
    "scan",
    "initialize"
]


def detect(command):

    command = command.lower()

    for word in OPEN_WORDS:
        if word in command:
            return Intent.OPEN

    for word in CLOSE_WORDS:
        if word in command:
            return Intent.CLOSE

    for word in PLAY_WORDS:
        if word in command:
            return Intent.PLAY

    for word in SEARCH_WORDS:
        if word in command:
            return Intent.SEARCH

    for word in REMEMBER_WORDS:
        if word in command:
            return Intent.REMEMBER

    for word in FORGET_WORDS:
        if word in command:
            return Intent.FORGET

    for word in SCAN_WORDS:
        if word in command:
            return Intent.SCAN

    return Intent.UNKNOWN