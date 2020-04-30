from pyfbsdk import *


'''
Creates a test cube at the given position on the XY plane, scaling it
uniformly by the given scale factor. The name of the cube will be
based on its initial position. Returns the new cube.
'''
##name = 'Cube' #% (xPos, yPos)
##cube = FBModelCube(name)
##cube.Show = True
##cube.Translation = FBVector3d(10, 10, 0.0)
##cube.Scaling = FBVector3d(10, 10, 10)
##print(cube.Scaling)

##name = 'CubeOne' #% (xPos, yPos)
##cube = FBModelCube(name)
##cube.Show = True
##cube.Translation = FBVector3d(30, 0, 0.0)
##cube.Scaling = FBVector3d(10, 10, 10)
##print(cube.Scaling)

myCube1 = FBFindModelByLabelName('CubeOne')
#myCube1.Scaling = FBVector3d(10, 10, 10)

print(myCube1.Scaling)