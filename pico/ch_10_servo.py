from machine import Pin, PWM
from utime import sleep

button_up = Pin(14, Pin.IN, Pin.PULL_UP)
button_down = Pin(15, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(16))
servo.freq(50) # pulse every 20ms

def set_angle(angle, min_pulse_us=500, max_pulse_us=2500):
    us_per_degree = (max_pulse_us - min_pulse_us) / 180
    pulse_us = us_per_degree * angle + min_pulse_us
    # duty 0 to 1023. At 50Hz, each duty_point is 20000/65535 = 0.305 µs/duty_point
    duty = int(pulse_us / 0.305)
    # print("angle=" + str(angle) + " pulse_us=" + str(pulse_us) + " duty=" + str(duty))
    print(angle)
    servo.duty_u16(duty)
    
angle = 90
set_angle(90)
min_angle = 10
max_angle = 160

while True:
    if button_up.value() == 0 and angle <= max_angle:
        angle += 1
        set_angle(angle)
        #print(angle)
        sleep(0.01)
    elif button_down.value() == 0 and angle > min_angle:
        angle -= 1
        set_angle(angle)
        #print(angle)
        sleep(0.01)