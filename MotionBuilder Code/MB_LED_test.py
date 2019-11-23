import time
try:
    import serial
except:
    import sys
    sys.path.append( "D:\Program Files (x86)\Python27\Lib\site-packages")
    import serial
    
ser = serial.Serial('COM3', 9600, timeout=1)

for i in range(10):
    ser.writelines(b'H')
    time.sleep(0.5)
    ser.writelines(b'L')
    time.sleep(0.5)

ser.close()

exit()