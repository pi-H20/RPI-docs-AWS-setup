# External module imp
import RPi.GPIO as GPIO
import time

# This file will contain all the method calls to water the plant

init = False

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme,

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def pump_on(pump_pin = 4, delay = 5):
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)

pump_on()