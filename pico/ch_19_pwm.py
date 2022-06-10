from machine import Pin, PWM
from utime import sleep

led = PWM(Pin(16))

while True:
    brightness_str = input("brightness (0-65534):")
    brightness = int(brightness_str)
    led.duty_u16(brightness)
    