import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)

'''

GPIO.setmode(GPIO.BOARD)

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

time.sleep(.5)

GPIO.output(4, GPIO.HIGH)

time.sleep(.5)

GPIO.output(4, GPIO.LOW)

time.sleep(.5)

GPIO.output(17, GPIO.HIGH)

time.sleep(.5)

GPIO.output(17, GPIO.LOW)
'''
