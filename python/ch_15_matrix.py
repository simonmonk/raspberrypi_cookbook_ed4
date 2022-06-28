import board
from adafruit_ht16k33.matrix import Matrix8x8x2
from time import sleep
from random import randint

i2c = board.I2C()
display = Matrix8x8x2(i2c)
display.brightness = 0.5

while True:
    x = randint(0, 8)
    y = randint(0, 8)
    color = randint(0, 4)
    display[x, y] = color
    sleep(0.1)
