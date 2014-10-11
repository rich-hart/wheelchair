import RPi.GPIO as GPIO
import time


pin = 8
GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BOARD)
func = GPIO.gpio_function(pin)
print(func)