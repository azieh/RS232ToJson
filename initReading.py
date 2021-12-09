#!/usr/bin/python3.10

bashCommand = "pkill -f startReading.py"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
