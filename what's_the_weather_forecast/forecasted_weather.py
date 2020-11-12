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
        forecasted_weather = owm_mgr.one_call(lat=lat, lon=lon).forecast_daily[0]
    except UnauthorizedError:
        tts.speak(
            "Invalid API key or key not activated yet. "
            "Verify e-mail address on OWM and try again in few minutes."
        )
        os.remove(wu.API_FILE)
        return

    tts.speak(f"According to daily forecasted weather,", rate=165)

    tts.speak(
        f"Tommorrow can be {forecasted_weather.detailed_status} outside.", rate=165
    )

    tts.speak(
        f"Temperatures can go from {forecasted_weather.temperature('celsius')['max']} degree celsius during the day, "
        f"to {forecasted_weather.temperature('celsius')['min']} degree celsius during night.",
        rate=165,
    )

    tts.speak(
        f"Humidity level can be {forecasted_weather.humidity} percent, and the predicted wind speed "
        f"is {round(forecasted_weather.wind('km_hour')['speed'], 1)} kilometers per hour "
        f"in {wu.getDirections(forecasted_weather.wnd['deg'])}.",
        rate=165,
    )

    if forecasted_weather.rain != {}:
        tts.speak(
            "There are chances of precipitation and it can rain tommorrow.", rate=165
        )

    if forecasted_weather.snow != {}:
        tts.speak("It can snow tommorrow.", rate=165)

    tts.speak(
        f"UV Index can be {forecasted_weather.uvi}, with {wu.getUVIndexRisk(forecasted_weather.uvi)} risk.",
        rate=165,
    )
