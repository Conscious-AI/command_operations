from utils import TTS, WebConnectivity

if __name__ == "__main__":
    tts = TTS()
    wc = WebConnectivity()

    if wc.is_connected():
        tts.speak("You are Online.", 125)
    else:
        tts.speak("You are Offline.", 125)
