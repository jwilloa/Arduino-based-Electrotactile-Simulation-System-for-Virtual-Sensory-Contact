from gloveFunctions import FiveDTGlove
import pdb

import sys
import time

# Locate module path
try:
    import serial
except:
    import sys
    sys.path.append( "C:\Python27\Lib\site-packages")
    import serial


#pdb.set_trace()
if __name__ == '__main__':
    while True:
        #pdb.set_trace()
        glove = FiveDTGlove()
        glove.open("USB0")
        glove.getSensorRawAll()


