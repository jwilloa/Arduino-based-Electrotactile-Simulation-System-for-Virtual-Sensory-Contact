from ctypes import *
import serial
import time
import Tkinter as tk
from Tkinter import *
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
        #pdb.set_trace()
        """Get a list of all the current raw sensor values."""
        arrTypeUShortArray20 = c_ushort*20
        sensorRawValues = arrTypeUShortArray20()     
        self.gloveDLL.fdGetSensorRawAll(self.glovePntr, sensorRawValues)
        numSensors = self.gloveDLL.fdGetNumSensors(self.glovePntr)
        global sensorRawValues
        #pdb.set_trace()
        #return list(sensorRawValues)

    def turnLED(self):
        ser = serial.Serial('COM5', 9600) 
        #print("Raw thumb sensor values: ", sensorRawValues[0])
        if sensorRawValues[0] >= 2500:
            #print "happy days"
            for i in range(3):
                ser.writelines(b'H')
                time.sleep(0.2)
        if sensorRawValues[3] >= 3400:
            #print "happy days"
            for i in range(3):
                ser.writelines(b'T')
                time.sleep(0.2)
        else:
            ser.writelines(b'L')
            
        #return list(sensorRawValues)


if __name__ == '__main__':
    while True:
##        root = Tk()
##        root.title("T7 CPU GUI")
##        root.geometry("300x300+700+300")
        glove = FiveDTGlove()
        glove.open("USB0")
        glove.getSensorRawAll()
        glove.turnLED()
        #print "Raw sensor values: " + str(glove.getSensorRawAll())
        print "Thumb: ", list(sensorRawValues)[0], "Index", list(sensorRawValues)[3]
        #print "Thumb" + list(sensorRawValues)[2]
