import time
from gpiozero import CPUTemperature
import requests

MAX_TEMP = 33.0
MIN_T_BETWEEN_WARNINGS = 60 # Minutes

EVENT = 'cpu_too_hot'
BASE_URL = 'https://maker.ifttt.com/trigger/'
KEY = 'your_key_here'

def send_notification(temp):
    data = {'value1' : temp}
    url = BASE_URL + EVENT + '/with/key/' + KEY
    response = requests.post(url, json=data)
    print(response.status_code)

def cpu_temp():
    cpu_temp = CPUTemperature().temperature
    return cpu_temp

while True:
    temp = cpu_temp()
    print("CPU Temp (C): " + str(temp))
    if temp > MAX_TEMP:
        print("CPU TOO HOT!")
        send_notification(temp)
        print("No more notifications for: " + str(MIN_T_BETWEEN_WARNINGS) + " mins")
        time.sleep(MIN_T_BETWEEN_WARNINGS * 60)
    time.sleep(1)

