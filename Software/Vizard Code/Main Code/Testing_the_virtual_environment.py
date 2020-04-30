import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Set up the environment and proximity sensors

dojo = viz.addChild('gallery.osgb')

#Create proximity manager and set debug on. Toggle debug with d key
manager = vizproximity.Manager()
manager.setDebug(viz.ON)
debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

#fade to true color when viewpoint moves near
def EnterSphere(e, sphere, color):
    sphere.runAction(vizact.fadeTo(color,time=1))

#fade to white when viewpoint moves away
def ExitSphere(e, sphere):
    sphere.runAction(vizact.fadeTo(viz.WHITE,time=1))

#add spheres and create a proximity sensor around each one
sphereSensors = []
def AddSphere(name, color, position):

    sphere = vizshape.addSphere(radius=0.2)
    sphere.setPosition(position)

    sensor = vizproximity.addBoundingSphereSensor(sphere,scale=0.7)
    sensor.name = name
    sphereSensors.append(sensor)
    manager.addSensor(sensor)

    manager.onEnter(sensor, EnterSphere, sphere, color)
    manager.onExit(sensor, ExitSphere, sphere)

AddSphere('red', viz.RED, [0,8
,4])
AddSphere('blue', viz.BLUE, [3.5,1.8,2])
AddSphere('yellow', viz.YELLOW, [3.5,1.8,-2])
AddSphere('green', viz.GREEN, [0,1.8,-4])
AddSphere('purple', viz.PURPLE, [-3.5,1.8,-2])
AddSphere('gray', viz.GRAY, [-3.5,1.8,2])

#Add a sensor in the center of the room for the participant to return to after each trial
centerSensor = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(0.0,0.0)),None)
manager.addSensor(centerSensor)

#Add vizinfo panel to display instructions
info = vizinfo.InfoPanel("Explore the environment\nPress 'd' to toggle the visibility of the sensors\nPress spacebar to begin the experiment")