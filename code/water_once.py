# External module imp
import RPi.GPIO as GPIO
import time

## This file executes the pump_on method to turn on

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme,

# setup to connect to the RPI
def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)


# This method sets the pump pin to turn on for 5 seconds
def pump_on(pump_pin = 4, delay = 5):
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)

# executes the method
pump_on()