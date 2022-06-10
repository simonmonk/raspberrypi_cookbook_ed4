from machine import Pin, ADC
from utime import sleep

temp_sensor = ADC(4)
points_per_volt = 3.3 / 65535

def read_temp_c():
    reading = temp_sensor.read_u16() * points_per_volt
    temp_c = 27 - (reading - 0.706)/0.001721
    return temp_c

while True:
    temp_c = read_temp_c()
    print(temp_c)
    sleep(0.5)


