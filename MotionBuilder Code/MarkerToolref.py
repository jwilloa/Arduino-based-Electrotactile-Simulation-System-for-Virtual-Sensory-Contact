from pyfbsdk import *
from pyfbsdk_additions import *
from random import *
 
MarkerTools = FBLabel()
MarkerCreateButton = FBButton()
SizeLabel = FBLabel()
SizeInput = FBEdit()
 
bMarkerCreateButton = FBButton()
 
## Check Boxes ---------------------
bMarkCube = FBButton()
bMarkHardCross = FBButton()
bMarkLightCross = FBButton()
bMarkSphere = FBButton()
bMarkCapsule = FBButton()
bMarkBox = FBButton()
bMarkBone = FBButton()
bMarkCircle = FBButton()
bMarkSquare = FBButton()
bMarkStick = FBButton()
bMarkNone = FBButton()
bMarkRigidgoal = FBButton()
bMarkRotationgoal = FBButton()
bMarkAimRollgoal = FBButton()
 
## Create Marker Button
def BtnCallbackbMarkerCreateButton(control, event):
    lR = random()
    lG = random()
    lB = random()
 
## Create Helper
lHelper = FBModelMarker('Helper_Mark 1')
lHelper.Show = True
lHelperSize = 1000
lHelper.Size = lHelperSize
 
## Define the look of the Marker
if bMarkCube.State == True:
    lMarkerLook = 0
if bMarkHardCross.State == True:
    lMarkerLook = 1
if bMarkLightCross.State == True:
    lMarkerLook = 2
if bMarkSphere.State == True:
    lMarkerLook = 3
if bMarkCapsule.State == True:
    lMarkerLook = 4
if bMarkBox.State == True:
    lMarkerLook = 5
if bMarkBone.State == True:
    lMarkerLook = 6
if bMarkCircle.State == True:
    lMarkerLook = 7
if bMarkSquare.State == True:
    lMarkerLook = 8
if bMarkStick.State == True:
    lMarkerLook = 9
if bMarkNone.State == True:
    lMarkerLook = 10
if bMarkRigidgoal.State == True:
    lMarkerLook = 11
if bMarkRotationgoal.State == True:
    lMarkerLook = 12
if bMarkAimRollgoal.State == True:
    lMarkerLook = 13
 
## Fail safe for if no check boxes are marked (default to cube)
if bMarkCube.State == bMarkHardCross.State == bMarkLightCross.State == bMarkSphere.State == bMarkCapsule.State == bMarkBox.State == bMarkBone.State == bMarkCircle.State == bMarkSquare.State == bMarkStick.State == bMarkNone.State == bMarkRigidgoal.State == bMarkRotationgoal.State == bMarkAimRollgoal.State == False:
lMarkerLook = 0
 
print 'No Marker Choice Made - Defaulting to "Cube" visual'
 
## Set LookUi to be that of the users choice
lHelper.PropertyList.Find('LookUi').Data = lMarkerLook
 
## Set the color for the helper using our random generated numbers defined above
lHelper.Color = FBColor(lR,lG,lB)
 
## ui look check box decision
 
## Cube
def BtnCallbackbMarkCube(control, event):
if bMarkCube.State == True:
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Hard Cross
def BtnCallbackbMarkHardCross(control, event):
if bMarkHardCross.State == True:
bMarkCube.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Lighgt Cross
def BtnCallbackbMarkLightCross(control, event):
if bMarkLightCross.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Sphere
def BtnCallbackbMarkSphere(control, event):
if bMarkSphere.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Capsule
def BtnCallbackbMarkCapsule(control, event):
if bMarkCapsule.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
# Box
def BtnCallbackbMarkBox(control, event):
if bMarkBox.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Bone
def BtnCallbackbMarkBone(control, event):
if bMarkBone.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Circle
def BtnCallbackbMarkCircle(control, event):
if bMarkCircle.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Square
def BtnCallbackbMarkSquare(control, event):
if bMarkSquare.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Stick
def BtnCallbackbMarkStick(control, event):
if bMarkStick.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## None
def BtnCallbackbMarkNone(control, event):
if bMarkNone.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Rigid Goal
def BtnCallbMarkRigidgoal(control, event):
if bMarkRigidgoal.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkAimRollgoal.Enabled = False
bMarkRotationgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRotationgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Rotational Goal
def BtnCallbackbMarkRotationgoal(control, event):
if bMarkRotationgoal.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRigidgoal.Enabled = False
bMarkAimRollgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkAimRollgoal.Enabled = True
 
## Aim Roll Goal
def BtnCallbackbMarkAimRollgoal(control, event):
if bMarkAimRollgoal.State == True:
bMarkCube.Enabled = False
bMarkHardCross.Enabled = False
bMarkLightCross.Enabled = False
bMarkSphere.Enabled = False
bMarkCapsule.Enabled = False
bMarkBox.Enabled = False
bMarkBone.Enabled = False
bMarkCircle.Enabled = False
bMarkSquare.Enabled = False
bMarkStick.Enabled = False
bMarkNone.Enabled = False
bMarkRotationgoal.Enabled = False
bMarkRigidgoal.Enabled = False
else:
bMarkCube.Enabled = True
bMarkHardCross.Enabled = True
bMarkLightCross.Enabled = True
bMarkSphere.Enabled = True
bMarkCapsule.Enabled = True
bMarkBox.Enabled = True
bMarkBone.Enabled = True
bMarkCircle.Enabled = True
bMarkSquare.Enabled = True
bMarkStick.Enabled = True
bMarkNone.Enabled = True
bMarkRigidgoal.Enabled = True
bMarkRotationgoal.Enabled = True
 
## Tool Window Creation
def PopulateTool(t):
 
#populate regions here
 
# Checkboxs for Character Process Type
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(20,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkCube","bMarkCube", x, y, w, h)
 
tMark.SetControl("bMarkCube", bMarkCube)
bMarkCube.Visible = True
bMarkCube.ReadOnly = False
bMarkCube.Enabled = True
bMarkCube.Hint = ""
bMarkCube.Caption = "Cube"
bMarkCube.State = 0
bMarkCube.Style = FBButtonStyle.kFBCheckbox
bMarkCube.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkCube.Look = FBButtonLook.kFBLookNormal
bMarkCube.OnClick.Add(BtnCallbackbMarkCube)
 
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(50,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkHardCross","bMarkHardCross", x, y, w, h)
 
tMark.SetControl("bMarkHardCross", bMarkHardCross)
bMarkHardCross.Visible = True
bMarkHardCross.ReadOnly = False
bMarkHardCross.Enabled = True
bMarkHardCross.Hint = ""
bMarkHardCross.Caption = "Hard Cross"
bMarkHardCross.State = 0
bMarkHardCross.Style = FBButtonStyle.kFBCheckbox
bMarkHardCross.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkHardCross.Look = FBButtonLook.kFBLookNormal
bMarkHardCross.OnClick.Add(BtnCallbackbMarkHardCross)
 
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(80,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkLightCross","bMarkLightCross", x, y, w, h)
 
tMark.SetControl("bMarkLightCross", bMarkLightCross)
bMarkLightCross.Visible = True
bMarkLightCross.ReadOnly = False
bMarkLightCross.Enabled = True
bMarkLightCross.Hint = ""
bMarkLightCross.Caption = "Light Cross"
bMarkLightCross.State = 0
bMarkLightCross.Style = FBButtonStyle.kFBCheckbox
bMarkLightCross.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkLightCross.Look = FBButtonLook.kFBLookNormal
bMarkLightCross.OnClick.Add(BtnCallbackbMarkLightCross)
 
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(110,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkSphere","bMarkSphere", x, y, w, h)
 
tMark.SetControl("bMarkSphere", bMarkSphere)
bMarkSphere.Visible = True
bMarkSphere.ReadOnly = False
bMarkSphere.Enabled = True
bMarkSphere.Hint = ""
bMarkSphere.Caption = "Sphere"
bMarkSphere.State = 0
bMarkSphere.Style = FBButtonStyle.kFBCheckbox
bMarkSphere.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkSphere.Look = FBButtonLook.kFBLookNormal
bMarkSphere.OnClick.Add(BtnCallbackbMarkSphere)
 
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkCapsule","bMarkCapsule", x, y, w, h)
 
tMark.SetControl("bMarkCapsule", bMarkCapsule)
bMarkCapsule.Visible = True
bMarkCapsule.ReadOnly = False
bMarkCapsule.Enabled = True
bMarkCapsule.Hint = ""
bMarkCapsule.Caption = "Capsule"
bMarkCapsule.State = 0
bMarkCapsule.Style = FBButtonStyle.kFBCheckbox
bMarkCapsule.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkCapsule.Look = FBButtonLook.kFBLookNormal
bMarkCapsule.OnClick.Add(BtnCallbackbMarkCapsule)
 
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(170,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkBox","bMarkBox", x, y, w, h)
 
tMark.SetControl("bMarkBox", bMarkBox)
bMarkBox.Visible = True
bMarkBox.ReadOnly = False
bMarkBox.Enabled = True
bMarkBox.Hint = ""
bMarkBox.Caption = "Box"
bMarkBox.State = 0
bMarkBox.Style = FBButtonStyle.kFBCheckbox
bMarkBox.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkBox.Look = FBButtonLook.kFBLookNormal
bMarkBox.OnClick.Add(BtnCallbackbMarkBox)
 
x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkBone","bMarkBone", x, y, w, h)
 
tMark.SetControl("bMarkBone", bMarkBone)
bMarkBone.Visible = True
bMarkBone.ReadOnly = False
bMarkBone.Enabled = True
bMarkBone.Hint = ""
bMarkBone.Caption = "Bone"
bMarkBone.State = 0
bMarkBone.Style = FBButtonStyle.kFBCheckbox
bMarkBone.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkBone.Look = FBButtonLook.kFBLookNormal
bMarkBone.OnClick.Add(BtnCallbackbMarkBone)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(20,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkCircle","bMarkCircle", x, y, w, h)
 
tMark.SetControl("bMarkCircle", bMarkCircle)
bMarkCircle.Visible = True
bMarkCircle.ReadOnly = False
bMarkCircle.Enabled = True
bMarkCircle.Hint = ""
bMarkCircle.Caption = "Circle"
bMarkCircle.State = 0
bMarkCircle.Style = FBButtonStyle.kFBCheckbox
bMarkCircle.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkCircle.Look = FBButtonLook.kFBLookNormal
bMarkCircle.OnClick.Add(BtnCallbackbMarkCircle)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(50,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkSquare","bMarkSquare", x, y, w, h)
 
tMark.SetControl("bMarkSquare", bMarkSquare)
bMarkSquare.Visible = True
bMarkSquare.ReadOnly = False
bMarkSquare.Enabled = True
bMarkSquare.Hint = ""
bMarkSquare.Caption = "Square"
bMarkSquare.State = 0
bMarkSquare.Style = FBButtonStyle.kFBCheckbox
bMarkSquare.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkSquare.Look = FBButtonLook.kFBLookNormal
bMarkSquare.OnClick.Add(BtnCallbackbMarkSquare)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(80,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkStick","bMarkStick", x, y, w, h)
 
tMark.SetControl("bMarkStick", bMarkStick)
bMarkStick.Visible = True
bMarkStick.ReadOnly = False
bMarkStick.Enabled = True
bMarkStick.Hint = ""
bMarkStick.Caption = "Stick"
bMarkStick.State = 0
bMarkStick.Style = FBButtonStyle.kFBCheckbox
bMarkStick.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkStick.Look = FBButtonLook.kFBLookNormal
bMarkStick.OnClick.Add(BtnCallbackbMarkStick)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(110,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkNone","bMarkNone", x, y, w, h)
 
tMark.SetControl("bMarkNone", bMarkNone)
bMarkNone.Visible = True
bMarkNone.ReadOnly = False
bMarkNone.Enabled = True
bMarkNone.Hint = ""
bMarkNone.Caption = "None"
bMarkNone.State = 0
bMarkNone.Style = FBButtonStyle.kFBCheckbox
bMarkNone.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkNone.Look = FBButtonLook.kFBLookNormal
bMarkNone.OnClick.Add(BtnCallbackbMarkNone)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkRigidgoal","bMarkRigidgoal", x, y, w, h)
 
tMark.SetControl("bMarkRigidgoal", bMarkRigidgoal)
bMarkRigidgoal.Visible = True
bMarkRigidgoal.ReadOnly = False
bMarkRigidgoal.Enabled = True
bMarkRigidgoal.Hint = ""
bMarkRigidgoal.Caption = "Rigid goal"
bMarkRigidgoal.State = 0
bMarkRigidgoal.Style = FBButtonStyle.kFBCheckbox
bMarkRigidgoal.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkRigidgoal.Look = FBButtonLook.kFBLookNormal
bMarkRigidgoal.OnClick.Add(BtnCallbMarkRigidgoal)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(170,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkRotationgoal","bMarkRotationgoal", x, y, w, h)
 
tMark.SetControl("bMarkRotationgoal", bMarkRotationgoal)
bMarkRotationgoal.Visible = True
bMarkRotationgoal.ReadOnly = False
bMarkRotationgoal.Enabled = True
bMarkRotationgoal.Hint = ""
bMarkRotationgoal.Caption = "Rotational goal"
bMarkRotationgoal.State = 0
bMarkRotationgoal.Style = FBButtonStyle.kFBCheckbox
bMarkRotationgoal.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkRotationgoal.Look = FBButtonLook.kFBLookNormal
bMarkRotationgoal.OnClick.Add(BtnCallbackbMarkRotationgoal)
 
x = FBAddRegionParam(140,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(35,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("bMarkAimRollgoal","bMarkAimRollgoal", x, y, w, h)
 
tMark.SetControl("bMarkAimRollgoal", bMarkAimRollgoal)
bMarkAimRollgoal.Visible = True
bMarkAimRollgoal.ReadOnly = False
bMarkAimRollgoal.Enabled = True
bMarkAimRollgoal.Hint = ""
bMarkAimRollgoal.Caption = "Aim/Roll goal"
bMarkAimRollgoal.State = 0
bMarkAimRollgoal.Style = FBButtonStyle.kFBCheckbox
bMarkAimRollgoal.Justify = FBTextJustify.kFBTextJustifyLeft
bMarkAimRollgoal.Look = FBButtonLook.kFBLookNormal
bMarkAimRollgoal.OnClick.Add(BtnCallbackbMarkAimRollgoal)
 
## ----------------------------------------------------------------
 
x = FBAddRegionParam(0,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(0,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(270,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(30,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("MarkerTools","MarkerTools", x, y, w, h)
 
tMark.SetControl("MarkerTools", MarkerTools)
MarkerTools.Visible = True
MarkerTools.ReadOnly = False
MarkerTools.Enabled = True
MarkerTools.Hint = ""
MarkerTools.Caption = "MarkerTool"
MarkerTools.Style = FBTextStyle.kFBTextStyleBold
MarkerTools.Justify = FBTextJustify.kFBTextJustifyCenter
MarkerTools.WordWrap = False
 
x = FBAddRegionParam(4,FBAttachType.kFBAttachNone,"")
y = FBAddRegionParam(240,FBAttachType.kFBAttachNone,"")
w = FBAddRegionParam(260,FBAttachType.kFBAttachNone,"")
h = FBAddRegionParam(55,FBAttachType.kFBAttachNone,"")
tMark.AddRegion("MarkerCreateButton","MarkerCreateButton", x, y, w, h)
 
tMark.SetControl("MarkerCreateButton", MarkerCreateButton)
MarkerCreateButton.Visible = True
MarkerCreateButton.ReadOnly = False
MarkerCreateButton.Enabled = True
MarkerCreateButton.Hint = ""
MarkerCreateButton.Caption = "Create"
MarkerCreateButton.State = 0
MarkerCreateButton.Style = FBButtonStyle.kFBPushButton
MarkerCreateButton.Justify = FBTextJustify.kFBTextJustifyCenter
MarkerCreateButton.Look = FBButtonLook.kFBLookNormal
MarkerCreateButton.OnClick.Add(BtnCallbackbMarkerCreateButton)
 
def CreateTool():
global tMark
tMark = FBCreateUniqueTool("MarkerTool v 0.1")
tMark.StartSizeX = 285
tMark.StartSizeY = 340
PopulateTool(tMark)
ShowTool(tMark)
CreateTool()