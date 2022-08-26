from machine import Pin, ADC
from utime import sleep

log_file = 'temp_readings.txt'
temp_sensor = ADC(4)
points_per_volt = 3.3 / 65535

def read_temp_c():
    reading = temp_sensor.read_u16() * points_per_volt
    temp_c = 27 - (reading - 0.706)/0.001721
    return temp_c

def log_data(reading):
    print(temp_c)
    file.write(str(reading)+'\n')
    
file = open(log_file, "w")
try:
    while True:
        temp_c = read_temp_c()
        log_data(temp_c)
        sleep(10)
except:
    print('Logging Ended')
    file.close()