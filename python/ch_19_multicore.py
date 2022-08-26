from utime import sleep
import _thread
from random import randint

def core0():
    while True:
        print("core 0 says hello")
        sleep(randint(1, 3))
        
def core1():
    while True:
        print("core 1 says hello")
        sleep(randint(1, 3))

_thread.start_new_thread(core1, ( ))
core0()