from win32 import win32clipboard as cb

from utils import TTS

tts = TTS()


def main():
    cb.OpenClipboard()
    try:
        cb_data = cb.GetClipboardData()
        if not cb_data.strip():
            tts.speak("Nothing to speak on clipboard.")
            return
        tts.speak("Speaking Clipboard")
        tts.speak(cb_data, 150)
    except TypeError:
        tts.speak("There's a file or folder copied on clipboard.", 175)
    cb.CloseClipboard()
