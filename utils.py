from typing import Tuple


class Interact:
    """
    This class can be used by the command scripts to take input
    from the user in an interactive way and produce any outputs
    through logger.
    """

    def __init__(self):
        import sys

        self.sys = sys

    def take_input(self, _str: str) -> str:
        self.sys.stdout.write(f"CAI: COPS: STDIN: {_str}\n")
        self.sys.stdout.flush()

        _in_str = self.sys.stdin.readline()

        if _in_str.isspace():
            _in_str = self.sys.stdin.readline()

        return _in_str

    def take_input_time(self, _str: str) -> str:
        return self.take_input(f"TIME: {_str}")


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

    def is_connected(self) -> bool:
        try:
            self.socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False


class LocationProvider:
    """
    A class that fetches current user location in realtime based on
    info provided by https://ip-api.com/
    """

    def __init__(self):
        import json
        import requests

        response = requests.get("http://ip-api.com/json/")
        self.data = json.loads(response.text)

    def get_location_info(self) -> Tuple[str, str, str]:
        return self.data["country"], self.data["regionName"], self.data["city"]

    def get_country_code(self) -> str:
        return self.data["countryCode"]

    def get_zip_code(self) -> int:
        return self.data["zip"]

    def get_location_coordinates(self) -> Tuple[int, int]:
        return self.data["lat"], self.data["lon"]

    def get_location_timezone(self) -> str:
        return self.data["timezone"]

