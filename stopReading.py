#!/usr/bin/python3.10

import time
bashCommand = "pkill -f startReading.py"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

import endVoteSesion

endVoteSesion