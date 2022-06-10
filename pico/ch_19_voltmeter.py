from machine import ADC, Pin
from utime import sleep

analog = ADC(26)

def volts_from_reading(reading):
    min_reading = 336
    max_reading = 65534
    reading_span = max_reading - min_reading
    volts_per_reading = 3.3 / reading_span
    volts = (reading - min_reading) * volts_per_reading
    return volts

while True:
    reading = analog.read_u16()
    print(volts_from_reading(reading))
    sleep(0.5)