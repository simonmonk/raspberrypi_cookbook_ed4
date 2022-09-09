from pmon import PlantMonitor
import time

time.sleep(2) # PlantMonitor startup time

pm = PlantMonitor()

while True:
    w = pm.get_wetness()
    t = pm.get_temp()
    h = pm.get_humidity()
    print("Wetness: {0} Temp: {1} Humidity: {2}".format(w, t, h))
    time.sleep(1)