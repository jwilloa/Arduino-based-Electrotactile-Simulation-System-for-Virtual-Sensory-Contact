# Import module to gain access to enture Vizard Code library
import viz
import vizact
import time
		
import viztracker
import hand

viz.setMultiSample(4)
viz.fov(60)
viz.go()# Start an empty world


#Identify the data glove's port.
PORT_5DT_USB = 0


#Add the 5DT sensor
sensor = viz.addSensor('5dt.dls')

#Create a hand object from the data glove
glove = hand.add(sensor,hand.GLOVE_5DT)
glove.setPosition([0,1.5,0.2])

#Place the hand in front of the user
glove.setEuler([0,-90,0])
viz.MainView.setPosition([0,0.02,-0.4])


#Add an array with all the gesture names from the 5DT user's manual.
gestureName = ['Fist', 'Index finger point', 'Middle finger point',
'Two finger point', 'Ring finger point', 'Ring-Index finger point',
'Ring-middle finger point', 'Three finger point', 'Little finger point',
'Index and little finger point', 'Little-middle finger point',
'Not ring finger point', 'Little-ring finger point',
'Not middle finger point', 'Not index finger point',
'Flat hand', 'Undefined']

#gestureText = viz.addText( '', viz.SCREEN )
#gestureText.setPosition(0.5,0.1)
#gestureText.alignment(viz.ALIGN_CENTER)

#def getGesture():
#    gesture = int(sensor.get()[-1])
#    gestureText.message(gestureName[gesture])
#    if gesture == 0:
#        print "closed fist"
#    if gesture == 15:
#        print "open hand"
#vizact.ontimer(0, getGesture)






gallery = viz.addChild( 'ground.osgb')								# Add a model of a gallery into the virtual world
viz.collision(viz.ON)												# Stop navigation through 3D models

hand = viz.add('white_ball.wrl')										# Add the object that will do the grabbing

# Link the hand to a 3D mousetracker
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
viz.link(mouseTracker,hand)

viz.mouse(viz.OFF)													# Disable mouse navigation

# Add a box model and set its position
basketball = viz.addChild('basketball.osgb')
basketball.setPosition([0,2,1.5])

ser = serial.Serial('COM5', 9600, timeout=1) 						# Open serial channel or selected port

link = None 														# The handle to the link object
													
def grabBall():
	object = viz.pick() 											# Command detects which object the mouse is currently over and returns it
	
	if object == basketball:										# Check to see if object is basketball
		print "You've clicked on the basketball"
		ser.writelines(b'T')										# Turn led/thumb electrode on
		global link
		link = viz.grab( hand, basketball ) 						# Use hand to grab basketball
	else:
		print "This is not a basketball"
		
def releaseBall():
	global link
	print "You have released the ball"
	link.remove()
	link = None
	ser.writelines(b'L')
		
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,grabBall)					# When left mouse button is clicked, go to pickBall function
vizact.onmouseup(viz.MOUSEBUTTON_LEFT,releaseBall)