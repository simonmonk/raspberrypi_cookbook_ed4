from gpiozero import CPUTemperature
import time
from bottle import route, run, template

def cpu_temp():
    cpu_temp = CPUTemperature()
    return str(cpu_temp.temperature)

@route('/temp')
def temp():
    return cpu_temp()
	
@route('/')
def index():
	return template('main.html')
	
@route('/raphael')
def index():
	return template('raphael.2.1.0.min.js')

@route('/justgage')
def index():
	return template('justgage.1.0.1.min.js')

run(host='0.0.0.0', port=80)
