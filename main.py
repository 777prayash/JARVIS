import time

from core.speech import speak
from core.listen import listen
from core.brain import process

speak("Hello Prayash. I am Jarvis.")

while True:

    command = listen()

    if command == "":
        continue

    command = command.lower().strip()

    # Greetings
    if "hello" in command or "hi" in command or "hey jarvis" in command:
        speak("Hello Prayash!")
        continue

    # How are you
    elif ("how are you" in command
          or "how r u" in command
          or "how are u" in command):
        speak("I am doing great. Thank you for asking!")
        continue

    # Name
    elif "your name" in command:
        speak("My name is Jarvis.")
        continue

    # Time
    elif "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        continue

    # Date
    elif "date" in command:
        current_date = time.strftime("%d %B %Y")
        speak(f"Today is {current_date}")
        continue

    # Exit
    elif "bye" in command or "exit" in command:
        speak("Goodbye Prayash.")
        time.sleep(2)
        break

    # Everything else goes to the Brain
    result = process(command)

    if result == "greeting":
        speak("Hello Prayash!")

    elif result == "name":
        speak("My name is Jarvis.")

    elif result == "time":
        import time
        speak(time.strftime("%I:%M %p"))

    elif result == "date":
        import time
        speak(time.strftime("%d %B %Y"))

    elif result == "unknown":
        speak("Sorry Prayash, I don't know that command yet.")