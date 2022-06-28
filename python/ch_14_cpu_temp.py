import time
from gpiozero import CPUTemperature

while True:
    cpu_temp = CPUTemperature()
    print(cpu_temp.temperature)
    time.sleep(1)
