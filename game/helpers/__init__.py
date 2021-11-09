import sys
import time

def writer(string, delay = 0.25):
    for char in string:
        if(char == " "):
            time.sleep(0)
        else:
            time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\r")
    time.sleep(0.25)
