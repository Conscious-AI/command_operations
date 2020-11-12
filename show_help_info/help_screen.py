from utils import Interact, TTS


def main():
    _tts = TTS()
    _in = Interact()
    _tts.speak("Showing commands information table", rate=175)
    _in.take_input("DISPLAY_HELP_INFO")
    _tts.speak("A commands info table listing all commands and their descriptions.", rate=175)
