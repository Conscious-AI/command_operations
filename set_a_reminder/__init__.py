import os
import subprocess as sp

from utils import TTS, Interact


DETACHED_PROCESS = 0x00000008
PATH = os.path.dirname(os.path.realpath(__file__))


def main():
    interact = Interact()
    tts = TTS()

    tts.speak("What should i remind you about ?")
    in_topic = interact.take_input("What to remind about ?")

    tts.speak("In what time ?")
    in_time = interact.take_input_time("Select Time")

    # Starting a detached process
    sp.Popen(
        ["python", os.path.join(PATH, "reminder.py"), in_topic, in_time],
        creationflags=DETACHED_PROCESS,
        cwd=PATH,
    )

    tts.speak(f"Setting a reminder for {in_topic} on {in_time}.")


if __name__ == "__main__":
    main()
