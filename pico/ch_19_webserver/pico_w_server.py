from microdot import Microdot
import mm_wlan
from pmon import PlantMonitor

ssid = 'network name'
password = 'password'

html = """
<!DOCTYPE html>
<meta http-equiv="refresh" content="1" >
<html>
    <head> <title>My Plant</title> </head>
    <body>
        <h1>Pico W Plant Monitor</h1>
        <h2>Water: {water}</h2>
        <h2>Temp (C): {temp}</h2>
        <h2>Humidity: {humidity}</h2>
    </body>
</html>
"""
pm = PlantMonitor()
app = Microdot()
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    w = pm.get_wetness()
    t = pm.get_temp()
    h = pm.get_humidity()
    response = html.format(water=w, temp=t, humidity=h)
    return response, {'Content-Type': 'text/html'}

app.run(port=80)
