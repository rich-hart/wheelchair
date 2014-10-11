import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)

time.sleep(.5)

GPIO.output(5, GPIO.HIGH)

time.sleep(.5)

GPIO.output(5, GPIO.LOW)

time.sleep(.5)

GPIO.output(6, GPIO.HIGH)

time.sleep(.5)

GPIO.output(6, GPIO.LOW)

GPIO.cleanup()

