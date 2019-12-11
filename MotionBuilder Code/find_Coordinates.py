from pyfbsdk import *

#myCube = FBModelCube("cube")
#myCube.Show = True

##myCube = FBFindModelByLabelName("Cube")
##myCube.Selected = True
##cube1 = FBVector3d()
##myCube.GetVector(cube1)
##print cube1

''' Get glove vector co-ord'''
##scene = FBSystem().Scene
##
##gloveDevice = FBCreateObject("Browsing/Templates/Devices", "5DT DataGlove", "5DT DataGlove")
##gloveDevice.OnLine = True
##gloveDevice.Live = True
##scene.Devices.append(gloveDevice)
##
##GT = FBVector3d()
##gloveDevice.GetVector(GT, FBModelTransformationMatrix.kModelTranslation, True)
##
###Bind model template to T and R animation nodes
## mChannels[i].mModelTemplate->Bindings.Add(mChannels[i].mTAnimNode);
## mChannels[i].mModelTemplate->Bindings.Add(mChannels[i].mRAnimNode);
## }


##searchMode = True
##searchNS = True
##compList = FBComponentList()
##FBFindObjectsByName("Cube", compList)
##for component in compList:
##    print component.LongName
##    print component.Translation


myCube2 = FBFindModelByLabelName("Cube")
myCube2.Selected = True
cube2 = FBVector3d()


myCube2.GetVector(cube2)
print cube2

