import badger2040
from machine import ADC
from utime import sleep

badger = badger2040.Badger2040()
temp_sensor = ADC(4)
points_per_volt = 3.3 / 65535

def read_temp_c():
    reading = temp_sensor.read_u16() * points_per_volt
    temp_c = 27 - (reading - 0.706)/0.001721
    return temp_c

badger.font("bitmap8")

old_t = 0

while True:
    t = round(read_temp_c())
    if t != old_t:
        old_t = t
        badger.pen(255) 
        badger.clear()
        badger.pen(0)
        badger.text(str(t), 20, 10, scale=16)
        badger.text("o", 220, 5, scale=8)
        badger.text("C", 255, 20, scale=8)
        badger.update()
        sleep(5)