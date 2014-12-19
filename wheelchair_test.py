import RPi.GPIO as GPIO
import time



def Check_Channel(channel):
    time.sleep(.5)

    GPIO.output(channel, GPIO.LOW)

    time.sleep(.75)

    GPIO.output(channel, GPIO.HIGH)

'RPI Pins'    
FORDWARD_CHANNEL = 8
REVERSE_CHANNEL = 10
LEFT_CHANNEL = 12
RIGHT_CHANNEL = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(FORDWARD_CHANNEL, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(REVERSE_CHANNEL, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(LEFT_CHANNEL, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(RIGHT_CHANNEL, GPIO.OUT, initial=GPIO.HIGH)

#Check_Channel(FORDWARD_CHANNEL)
#Check_Channel(REVERSE_CHANNEL)
Check_Channel(LEFT_CHANNEL)
#Check_Channel(RIGHT_CHANNEL)

GPIO.cleanup()

