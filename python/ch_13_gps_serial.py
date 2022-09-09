import serial

ser = serial.Serial('/dev/serial0')

while True:
    line = ser.readline().decode("utf-8")
    message = line.split(',')
    if message[0] == '$GPRMC':
        if message[2] == 'A':
            lat = message[3] + message[4]
            lon = message[5] + message[6]
            print(F"lat={lat} \tlon={lon}")
        else:
            print("No fix")
