import serial
import time

# Open serial channel or selected port
ser = serial.Serial('COM3', 9600, timeout=1) 

# 10 second count of high/low signals
for i in range(10):
    ser.writelines(b'H')
    time.sleep(0.5)
    ser.writelines(b'L')
    time.sleep(0.5)

ser.close()

exit()
