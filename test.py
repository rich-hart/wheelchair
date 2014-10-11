import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

for i in range(1,41):
    lable = "????"
    func = GPIO.gpio_function(pin)
    if func == GPIO.INPUT:
        lable = "Input"
    elif func == GPIO.OUTPUT:
        lable = "Output"
    elif func == GPIO.SPI:
        lable = "SPI"
    elif func == GPIO.I2C:
        lable = "I2C"
    elif func == GPIO.HARD_PWM:
        lable = "HARD_PWM"
    elif func == GPIO.SERIAL:
        lable = "SERIAL"
    elif func == GPIO.UNKNOWN:
        lable = "UNKNOWN"
    print(str(i)+" "+lable)

