from gloveFunctions import FiveDTGlove
import pdb


#pdb.set_trace()
if __name__ == '__main__':
    while True:
        #pdb.set_trace()
        glove = FiveDTGlove()
        glove.open("USB0")
        glove.getSensorRawAll()
        glove.turnLED()

