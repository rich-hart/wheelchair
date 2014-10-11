import RPi.GPIO as GPIO
import time

FORDWARD_CHANNEL = 5
REVERSE_CHANNEL = 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(FORDWARD_CHANNEL, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(REVERSE_CHANNEL, GPIO.OUT, initial=GPIO.LOW)

time.sleep(.5)

GPIO.output(FORDWARD_CHANNEL, GPIO.HIGH)

time.sleep(.5)

GPIO.output(FORDWARD_CHANNEL, GPIO.LOW)

time.sleep(.5)

GPIO.output(REVERSE_CHANNEL, GPIO.HIGH)

time.sleep(.5)

GPIO.output(REVERSE_CHANNEL, GPIO.LOW)

GPIO.cleanup()

