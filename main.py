import time

from core.speech import speak
from core.listen import listen
from core.commands import execute

speak("Hello Prayash. I am Jarvis.")

while True:

    command = listen()

    if command == "":
        continue

    # Execute PC commands
    if execute(command):
        speak("Done.")
        continue

    # Greetings
    if "hello" in command or "hi" in command or "hey jarvis" in command:
        speak("Hello Prayash!")

    # How are you
    elif ("how are you" in command
          or "how r u" in command
          or "how are u" in command):
        speak("I am doing great. Thank you for asking!")

    # Name
    elif "your name" in command:
        speak("My name is Jarvis.")

    # Time
    elif "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Date
    elif "date" in command:
        current_date = time.strftime("%d %B %Y")
        speak(f"Today is {current_date}")

    # Exit
    elif "bye" in command or "exit" in command:
        speak("Goodbye Prayash.")
        time.sleep(2)
        break

    # Unknown command
    else:
        speak("Sorry, I don't know that command yet.")