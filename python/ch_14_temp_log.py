import glob, time, datetime
from gpiozero import CPUTemperature

log_period = 10 # seconds

logging_folder = glob.glob('/media/*')[0]
dt = datetime.datetime.now()
file_name = "temp_log_{:%Y_%m_%d}.csv".format(dt)
logging_file = logging_folder + '/' + file_name

def read_temp():
    cpu_temp = CPUTemperature().temperature
    return cpu_temp

def log_temp():
    temp_c = read_temp()
    dt = datetime.datetime.now()
    f = open(logging_file, 'a')
    line = '\n"{:%H:%M:%S}","{}"'.format(dt, temp_c)
    f.write(line)
    print(line)
    f.close()

print("Logging to: " + logging_file)
while True:
    log_temp()
    time.sleep(log_period)
