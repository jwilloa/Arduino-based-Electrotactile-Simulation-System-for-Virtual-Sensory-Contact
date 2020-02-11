#import viz
#import vizact
#import vizshape
#import vizinfo
#import hand
#
#viz.setMultiSample(4)
#viz.fov(60)
#viz.go()
#
#maze = viz.addChild('maze.osgb')
#
#BirdEyeWindow = viz.addWindow()
#BirdEyeWindow.fov(60)
#BirdEyeWindow.visible(0,viz.SCREEN)
#BirdEyeView = viz.addView()
#BirdEyeWindow.setView(BirdEyeView)
#BirdEyeView.setPosition([0,25,0])
#BirdEyeView.setEuler([0,90,0])
#
##Identify the data glove's port.
#PORT_5DT_USB = 0
#
##Add the 5DT sensor
#sensor = viz.addSensor('5dt.dls')
#
##Create a hand object from the data glove
#glove = hand.add(sensor,hand.GLOVE_5DT)
#
##Place the hand in front of the user
##glove.setEuler([0,-90,0])
##viz.MainView.setPosition([0,0.02,-0.4])
#
##box = vizshape.addBox(pos=positions[2],splitFaces=True)
#box.setEuler([0,-90,0])
#viz.MainView.setPosition([0,0.02,-0.4])
#box.color(viz.SKYBLUE)
#box.color(viz.PURPLE,'left')
#box.color(viz.PURPLE,'right')

"""
This script demonstrates the various kinds of
area shapes included with the vizproximity module.
Use the WASD keys to move the axes and trigger the sensors.
"""
import viz
import vizcam
import vizshape
import vizproximity
viz.go()
viz.fov(60)

import vizinfo
vizinfo.InfoPanel()

# Add axes controlled by keyboard
axis = vizshape.addAxes(length=0.5)
tracker = vizcam.addKeyboardPos()
viz.link(tracker,axis)

# Create manager tracked axes
manager = vizproximity.Manager()
manager.setDebug(True)
manager.addTarget(vizproximity.Target(tracker))

# Sensor callbacks
def onEnterSensor(e):
    print 'Entered',e.sensor.name

def onExitSensor(e):
    print 'Exited',e.sensor.name

manager.onEnter(None, onEnterSensor)
manager.onExit(None, onExitSensor)

def AddSensor(shape,name):
    sensor = vizproximity.Sensor(shape,None)
    sensor.name = name
    manager.addSensor(sensor)

# Add circle area
shape = vizproximity.CircleArea(0.5,center=[0,2])
AddSensor(shape,'Circle')

# Add rectangle area
shape = vizproximity.RectangleArea([2,1],center=[3,2])
AddSensor(shape,'Rectangle')

# Add polygon area
verts = [ (0,0), (1,1), (0,1.5), (-2,2), (-1,1), (-2,0.5) ]
shape = vizproximity.PolygonArea(verts,offset=[-3,1])
AddSensor(shape,'Polygon')

# Add path area
path = [ (0,0), (0,1), (1,2), (0,3), (-0.5,3), (-1,3), (-1,2) ]
shape = vizproximity.PathArea(path,radius=0.4,offset=[0,3.5])
AddSensor(shape,'Path')

# Setup environment
vizshape.addGrid(color=[0.2]*3,pos=(0,-0.01,0))
viz.clearcolor(viz.GRAY)

# Setup pivot navigation
import vizcam
cam = vizcam.PivotNavigate(distance=10,center=(0,0,3))
cam.rotateUp(60)
viz.cam.setHandler(cam)