class Interact:
    """
    This class can be used by the command scripts to take input
    from the user in an interactive way and produce any outputs
    through logger.
    """

    def __init__(self):
        import sys

        self.sys = sys

    def take_input(self, _str: str):
        self.sys.stdout.write(f"CAI: COPS: STDIN: {_str}\n")
        self.sys.stdout.flush()
        return self.sys.stdin.readline()


class TTS:
    """
    Text-to-speech utility class for simple auditory interaction with user.
    """

    def __init__(self):
        import pyttsx3

        self.engine = pyttsx3.init()

    def speak(self, _str: str, rate=200):
        self.engine.setProperty("rate", rate)
        self.engine.say(_str)
        self.engine.runAndWait()


class WebConnectivity:
    """
    A class for checking if the user's system is connected to the internet.
    """

    def __init__(self):
        import socket

        self.socket = socket

    def is_connected(self):
        try:
            self.socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False
