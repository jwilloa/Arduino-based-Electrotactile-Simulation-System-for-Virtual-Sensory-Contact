# Import module to gain access to enture Vizard library
import viz
import vizact
import time
import serial
import viztracker

viz.setMultiSample(4)
viz.fov(60)
viz.go()# Start an empty world


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

ser = serial.Serial('COM3', 9600, timeout=1) 						# Open serial channel or selected port

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
	link.remove()
	link = None
	ser.writelines(b'L')
		
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,grabBall)					# When left mouse button is clicked, go to pickBall function
vizact.onmouseup(viz.MOUSEBUTTON_LEFT,releaseBall)