from pyfbsdk import *
#import os
import time

### Access system properties
##scene = FBSystem().Scene
##
### Create a 5DT Glove device and append it to the scene.
##gloveDevice = FBCreateObject("Browsing/Templates/Devices", "5DT DataGlove", "5DT DataGlove")
##gloveDevice.OnLine = True
##gloveDevice.Live = True
##scene.Devices.append(gloveDevice)
##
##GT = FBVector3d()
##gloveDevice.GetVector(GT, FBModelTransformationMatrix.kModelTranslation, True)
##
###FBSystem&#40;&#41;.Scene.Evaluate()

name = 'Cube'
cube = FBFindModelByLabelName(name)
cube.Selected = True
cube.Translation = FBVector3d(10, 12, 10)

#print cube.Translation[1]
x = cube.Translation[1]
x = x + 1
##while x < 50:
##    cube.Translation = FBVector3d(10, x, 10)
##    #time.sleep(0.1)
##    x = x + 1

cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1
cube.Translation = FBVector3d(10, x, 10)
x = x + 1