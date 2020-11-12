import os

from pyowm import OWM
from pyowm.commons.exceptions import UnauthorizedError

from utils import Interact, TTS, WebConnectivity, LocationProvider, WeatherUtils


def main():
    _in = Interact()
    tts = TTS()
    wc = WebConnectivity()
    loc = LocationProvider()
    wu = WeatherUtils()

    if not wc.is_connected():
        tts.speak("You are not connected to an active internet connection")
        return

    if not os.path.isfile(wu.API_FILE):
        tts.speak(
            "Looks like this command is running for the first time, so you have to sign-up "
            "for a free API key on openweathermap.org. After signing-up, verify your e-mail address "
            "and then paste your key in the input box.",
            rate=150,
        )
        wu.owm_register(_in)

    with open(wu.API_FILE, "r") as f:
        key = f.readline().strip()

    owm = OWM(key)
    owm_mgr = owm.weather_manager()

    lat, lon = loc.get_location_coordinates()

    try:
        current_weather = owm_mgr.one_call(lat=lat, lon=lon).current
    except UnauthorizedError:
        tts.speak(
            "Invalid API key or key not activated yet. "
            "Verify e-mail address on OWM and try again in few minutes."
        )
        os.remove(wu.API_FILE)
        return

    tts.speak(f"It's {current_weather.detailed_status} outside.", rate=165)

    tts.speak(
        f"Currently it's {current_weather.temperature('celsius')['temp']} degree celsius.",
        rate=165,
    )

    tts.speak(
        f"Humidity level is {current_weather.humidity} percent, and the wind is flowing with "
        f"{round(current_weather.wind('km_hour')['speed'], 1)} kilometers per hour "
        f"in {wu.getDirections(current_weather.wnd['deg'])}.",
        rate=165,
    )

    tts.speak(
        f"UV index is {current_weather.uvi}, with {wu.getUVIndexRisk(current_weather.uvi)} risk.",
        rate=165,
    )
