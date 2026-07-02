import webbrowser
from core.speech import speak


def execute(command):

    command = command.lower().strip()

    # Google Search
    if command.startswith("search google for"):

        query = command.replace(
            "search google for", ""
        ).strip()

        speak(f"Searching Google for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return True

    # YouTube Search
    if command.startswith("search youtube for"):

        query = command.replace(
            "search youtube for", ""
        ).strip()

        speak(f"Searching YouTube for {query}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

        return True

    return False