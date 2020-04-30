import time
import sys

while True:
    sys.stdout.write("\\\\\r")
    time.sleep(.25)
    sys.stdout.flush()
    sys.stdout.write("--\r")
    sys.stdout.flush()
    sys.stdout.write("//\r")
    time.sleep(.25)
    sys.stdout.flush()
    sys.stdout.write("--\r")
    time.sleep(.25)
    sys.stdout.flush()

