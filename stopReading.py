#!/usr/bin/python3.6

import time
bashCommand = "pkill -f startReading.py"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

time.sleep(3)

import readBatteryStatus
import endVoteSesion
readBatteryStatus
endVoteSesion
