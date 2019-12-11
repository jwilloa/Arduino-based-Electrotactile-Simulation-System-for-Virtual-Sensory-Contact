from ctypes import *
import serial
import time
import pdb

class FiveDTGlove:
    def __init__(self):
        self._as_parameter_ = 5

        self.gloveDLL = cdll.LoadLibrary("fglove")
        if self.gloveDLL == None:
            raise IOError("Could not open fglove.dll")

    def open(self, port):
        self.glovePntr = 0;
        self.glovePntr = self.gloveDLL.fdOpen(port)
        if self.glovePntr == 0:
            raise IOError("Could not connect to 5DT glove.")            

    def getSensorRawAll(self):
        global sensorRawValues
        """Get a list of all the current raw sensor values."""
        arrTypeUShortArray20 = c_ushort*20
        sensorRawValues = arrTypeUShortArray20()     
        self.gloveDLL.fdGetSensorRawAll(self.glovePntr, sensorRawValues)
        numSensors = self.gloveDLL.fdGetNumSensors(self.glovePntr)
        print "Thumb: ", list(sensorRawValues)[0], "Index", list(sensorRawValues)[3], "Middle", list(sensorRawValues)[6], \
            "Ring", list(sensorRawValues)[9], "Little", list(sensorRawValues)[12]
        #return list(sensorRawValues)

    def turnLED(self):
        ser = serial.Serial('COM5', 9600)
        if sensorRawValues[0] >= 2500:
            for i in range(3):
                ser.writelines(b'T')
                time.sleep(0.2)
        if sensorRawValues[3] >= 3400:
            for i in range(3):
                ser.writelines(b'I')
                time.sleep(0.2)
        if sensorRawValues[7] >= 2500:
            for i in range(3):
                ser.writelines(b'M')
                time.sleep(0.2)
        if sensorRawValues[10] >= 2800:
            for i in range(3):
                ser.writelines(b'R')
                time.sleep(0.2)
        if sensorRawValues[13] >= 3000:
            for i in range(3):
                ser.writelines(b'L')
                time.sleep(0.2)
        else:
            ser.writelines(b'L')
            
        #return list(sensorRawValues)


# if __name__ == '__main__':
#     while True:
#         glove = FiveDTGlove()
#         glove.open("USB0")
#         glove.getSensorRawAll()
#         ##glove.turnLED()
#         #print "Raw sensor values: " + str(glove.getSensorRawAll())
#         print "Thumb: ", list(sensorRawValues)[0], "Index", list(sensorRawValues)[3]
#         #print "Thumb" + list(sensorRawValues)[2]
