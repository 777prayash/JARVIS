import webbrowser

from core.speech import speak


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
    "x": "https://x.com",
    "claude": "https://claude.ai",
    "gemini": "https://gemini.google.com",
    "perplexity": "https://www.perplexity.ai"
}


def execute(command):

    command = command.lower().strip()

    if command.startswith("open "):

        website = command.replace("open", "").strip()

        if website in WEBSITES:

            speak(f"Opening {website}")

            webbrowser.open(WEBSITES[website])

            return True

    return False