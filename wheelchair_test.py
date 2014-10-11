import RPi.GPIO as GPIO
import time



def Check_Channel(channel):
    time.sleep(.5)

    GPIO.output(channel, GPIO.HIGH)

    time.sleep(.5)

    GPIO.output(channel, GPIO.LOW)
    
FORDWARD_CHANNEL = 5
REVERSE_CHANNEL = 13
LEFT_CHANNEL = 19
RIGHT_CHANNEL = 26

GPIO.setmode(GPIO.BOARD)

GPIO.setup(FORDWARD_CHANNEL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(REVERSE_CHANNEL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEFT_CHANNEL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIGHT_CHANNEL, GPIO.OUT, initial=GPIO.LOW)

Check_Channel(FORDWARD_CHANNEL)
Check_Channel(REVERSE_CHANNEL)
Check_Channel(LEFT_CHANNEL)
Check_Channel(RIGHT_CHANNEL)

GPIO.cleanup()

