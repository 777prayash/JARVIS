from core.intent import detect


def parse(command):

    command = command.lower().strip()

    intent = detect(command)

    target = command

    for word in [
        "open",
        "launch",
        "start",
        "run",
        "play",
        "watch",
        "listen",
        "search",
        "find",
        "remember",
        "forget",
        "scan"
    ]:

        target = target.replace(word, "")

    target = target.strip()

    return {
        "intent": intent,
        "target": target,
        "text": command
    }