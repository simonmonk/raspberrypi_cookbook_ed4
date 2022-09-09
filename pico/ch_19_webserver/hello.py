from microdot import Microdot
import mm_wlan

ssid = 'my network name'
password = 'my passord'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    return 'Hello, from Pico'

app.run(port=80)