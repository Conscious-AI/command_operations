from win32 import win32clipboard as cb

from utils import TTS

tts = TTS()


def main():
    cb.OpenClipboard()
    try:
        cb.EmptyClipboard()
        cb.SetClipboardText("")
        tts.speak("Clipboard cleared successfully.")
    except:
        tts.speak("An error occured in clearing the clipboard")
    cb.CloseClipboard()
