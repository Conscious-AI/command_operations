import socket
import requests

from utils import TTS, WebConnectivity


def get_private_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    private_ipv4 = s.getsockname()[0]
    s.close()
    return private_ipv4


def get_public_ipv4():
    public_ipv4 = requests.get("https://checkip.amazonaws.com").text.strip()
    return public_ipv4


def main():
    tts = TTS()
    wc = WebConnectivity()

    tts.speak("Speaking your private and public IP addresses")
    tts.speak(f"Your private IP address is {get_private_ipv4()}", 150)
    if wc.is_connected():
        tts.speak(f"Your public IP address is {get_public_ipv4()}", 150)
    else:
        tts.speak("I can't fetch your public IP address currently.")


if __name__ == "__main__":
    main()
