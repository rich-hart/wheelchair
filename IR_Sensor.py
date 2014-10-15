import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
count = 0
while True:
    reading = ser.readline()
    print reading.strip()
    count = count +1
    if count>10:
        break;
ser.flush()
ser.close()