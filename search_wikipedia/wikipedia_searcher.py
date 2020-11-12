import wikipedia as wp

from utils import Interact, TTS, WebConnectivity


def wiki_summary(kw):
    return wp.summary(kw)


def main():
    _in = Interact()
    tts = TTS()
    wc = WebConnectivity()

    if not wc.is_connected():
        tts.speak("You are not connected to an active internet connection")
        return

    tts.speak("Enter a keyword to search Wikipedia")
    keyword = _in.take_input("Enter a keyword to search Wikipedia")
    tts.speak(f"Searching wikipedia for {keyword}")

    try:
        tts.speak(wiki_summary(keyword), rate=175)
    except wp.DisambiguationError:
        tts.speak(
            "Multiple query references found. Enter a more specific keyword and try again."
        )
    except wp.PageError:
        tts.speak("No matching query found on wikipedia.")
