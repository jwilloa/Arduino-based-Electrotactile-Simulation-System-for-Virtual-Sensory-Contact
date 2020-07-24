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
            
        return list(sensorRawValues)[9]
