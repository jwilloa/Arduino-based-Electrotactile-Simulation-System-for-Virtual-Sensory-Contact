import gloveFunctions
from gloveFunctions import FiveDTGlove
#from gloveFunctions import open
#from gloveFunctions import getSensorRawAll
import pdb


#pdb.set_trace()
if __name__ == '__main__':
    while True:
        #pdb.set_trace()
        glove = FiveDTGlove()
        glove.open("USB0")
        sensorRawValues = glove.getSensorRawAll()
        print sensorRawValues
        #print glove.getSensorRawAll(sensorRawValues)
        #print "Thumb: ", list(sensorRawValues)[0], "Index", list(sensorRawValues)[3]
