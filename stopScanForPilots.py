#!/usr/bin/python3.6

import readBatteryStatus
import endVoteSesion

bashCommand = "pkill -f startScanForPilots.py"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

readBatteryStatus
endVoteSesion
