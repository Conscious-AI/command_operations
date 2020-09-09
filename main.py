import os
import sys
import subprocess as sp

sys.path.append("..")

import pandas as pd

import utils
from command_recognizer import recognize_command as rc


_CSV_FILE = "..\\command_recognizer\\data\\command_labels.csv"


class CommandOps:
    def __init__(self):
        # TODO: Refactor
        self.command_csv = pd.read_csv(_CSV_FILE)
        self.command_dirs = self.command_csv.iloc[:, 0]
        self.command_labels = self.command_csv.iloc[:, 1]
        self.tts = utils.TTS()

    def run(self, _dir):
        sp.run(["python", f"{_dir}\\__init__.py"], cwd=_dir)

    def init(self):
        recognizer = rc.CommandRecognizer()
        while True:
            command, _ = recognizer.recognize()

            for i in range(len(self.command_labels)):
                if command == self.command_labels[i]:
                    if os.path.isdir(self.command_dirs[i]):
                        self.run(str(self.command_dirs[i]))
                    else:
                        self.tts.speak("Command recognized but logic not found.")


if __name__ == "__main__":
    cOps = CommandOps()
    cOps.init()
