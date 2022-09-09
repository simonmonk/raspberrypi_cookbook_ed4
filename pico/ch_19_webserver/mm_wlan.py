"""
mm_wlan
--------
The ``mm_wlan`` module defines a couple of methods to simplify connecting to a 
wireless network. https://github.com/monkmakes/mm_wlan

"""


import network, time

wlan = network.WLAN(network.STA_IF)

def connect_to_network(ssid, password, retries=10, verbose=True):
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # Disable power-save mode
    wlan.connect(ssid, password)
    if verbose: print('Connecting to ' + ssid, end=' ')
        
    while retries > 0 and wlan.status() != network.STAT_GOT_IP:
        retries -= 1
        if verbose: print('.', end='')
        time.sleep(1)    
        
    if wlan.status() != network.STAT_GOT_IP:
        if verbose: print('\nConnection failed. Check ssid and password')
        raise RuntimeError('WLAN connection failed')
    else:
        if verbose: print('\nConnected. IP Address = ' + wlan.ifconfig()[0])

def is_connected():
    return wlan.status() == network.STAT_GOT_IP