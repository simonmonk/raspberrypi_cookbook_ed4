import board
from adafruit_ht16k33.segments import Seg7x4
from time import sleep

i2c = board.I2C()
display = Seg7x4(i2c)
display.brightness = 0.5

x = 0

while True:
    display.print("    ")
    display.print(x)
    x += 1
    if x > 9999:
        x = 0
    sleep(1)

