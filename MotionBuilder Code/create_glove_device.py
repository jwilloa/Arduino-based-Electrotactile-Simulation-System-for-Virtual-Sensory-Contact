from pyfbsdk import *
import os

# Access system properties
scene = FBSystem().Scene

# Create a 5DT Glove device and append it to the scene.
gloveDevice = FBCreateObject("Browsing/Templates/Devices", "5DT DataGlove", "5DT DataGlove")
gloveDevice.OnLine = True
gloveDevice.Live = True
scene.Devices.append(gloveDevice)

GT = FBVector3d()
gloveDevice.GetVector(GT, FBModelTransformationMatrix.kModelTranslation, True)

#FBSystem&#40;&#41;.Scene.Evaluate()