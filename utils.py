class TTS:
    """
    Text-to-speech utility class for simple auditory interaction with user.
    """

    def __init__(self):
        import pyttsx3

        self.engine = pyttsx3.init()

    def speak(self, _str):
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
