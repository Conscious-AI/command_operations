import sys
import wave
import time as t
from datetime import datetime as dt

import pyaudio

sys.path.append("..")
from utils import TTS


def sleep_until(end_dt):
    while True:
        diff_t = (end_dt - dt.now()).total_seconds()
        if diff_t < 0:
            return
        t.sleep(diff_t / 2)
        if diff_t <= 0.1:
            return


def alerting_user():
    chunk = 1024

    f = wave.open("alert_high-intensity.wav", "rb")
    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(f.getsampwidth()),
        channels=f.getnchannels(),
        rate=f.getframerate(),
        output=True,
    )

    data = f.readframes(chunk)

    # Alerting with sound
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    # Cleaning up
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    tts = TTS()

    # Receiving arguments from init script
    _topic, _time = sys.argv[1], sys.argv[2]

    dt_now = dt.now()
    hrs, mins = _time.split(":")
    future_dt = dt(dt_now.year, dt_now.month, dt_now.day, int(hrs), int(mins))

    sleep_until(future_dt)

    alerting_user()

    tts.speak(f"Reminder ! Reminding you about {_topic}", rate=175)
