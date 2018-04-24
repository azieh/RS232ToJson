#!/usr/bin/python3.6
bashCommand = "pkill -f startReading.py"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()