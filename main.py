import os
import sys
import subprocess as sp
import asyncio

sys.path.append("..")

import pandas as pd

import utils
from command_recognizer import recognize_command as rc


PATH = os.path.dirname(os.path.realpath(__file__))
_CSV_FILE = "..\\command_recognizer\\data\\command_labels.csv"


def printout(_data):
    print(_data)
    sys.stdout.flush()


class CommandOps:
    def __init__(self):
        # TODO: Refactor
        self.command_csv = pd.read_csv(_CSV_FILE)
        self.command_dirs = self.command_csv.iloc[:, 0]
        self.command_labels = self.command_csv.iloc[:, 1]
        self.tts = utils.TTS()

    async def _handle_stream(self, streamIn, streamOut, in_cb, out_cb):
        while True:
            line = await streamOut.readline()
            if line:
                # Detecting if input is required
                if "CAI: COPS: STDIN" in str(line):
                    await in_cb(streamIn, line)
                else:
                    out_cb(line)
            else:
                break

    async def _stream_subprocess(self, cmd, stdin_cb, stdout_cb):
        process = await asyncio.create_subprocess_exec(
            *cmd, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE
        )
        await asyncio.wait(
            [self._handle_stream(process.stdin, process.stdout, stdin_cb, stdout_cb)]
        )
        return await process.wait()

    async def proc_input_cb(self, streamIn, line: bytes):
        printout(line.decode())

        # Sending user response back to process
        _in = sys.stdin.readline()
        streamIn.write(f"{_in}\r\n".encode())

        # Draining the stdin of process stream
        await streamIn.drain()

        # TODO: Close the StreamWriter

    def proc_output_cb(self, line: bytes):
        printout(f"Inside proc output callback - {line.decode()}")

    def run(self, _dir):
        # Running commands as separate modules
        args = ["python", "-m", f"{_dir}.__init__"]

        # Asynchronously execute and handle commmands by
        # running them in a seperate event loop
        asyncio.run(
            self._stream_subprocess(args, self.proc_input_cb, self.proc_output_cb)
        )

    def init(self):
        recognizer = rc.CommandRecognizer()
        while True:
            command, _ = recognizer.recognize()

            for i in range(len(self.command_labels)):
                if command == self.command_labels[i]:
                    printout(f"> IN:  {command}")
                    if os.path.isdir(self.command_dirs[i]):
                        self.run(str(self.command_dirs[i]).replace("/", ""))
                    else:
                        self.tts.speak("Command recognized but logic not found.")


if __name__ == "__main__":
    os.chdir(PATH)
    cOps = CommandOps()
    cOps.init()
