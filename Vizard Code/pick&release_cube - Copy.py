# Import module to gain access to enture Vizard Code library
import viz
import vizact
import time
import viztracker
from gloveFunctions import FiveDTGlove

viz.setMultiSample(4)
viz.fov(60)
viz.go()# Start an empty world
glove = FiveDTGlove()
glove.open("USB0")

gallery = viz.addChild( 'ground.osgb' )								# Add a model of a gallery into the virtual world
viz.collision(viz.ON)												# Stop navigation through 3D models


hand = viz.add('white_ball.wrl')									# Add the object that will do the grabbing

# Link the hand to a 3D mousetracker
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
viz.link(mouseTracker,hand)

viz.mouse(viz.OFF)													# Disable mouse navigation

# Link the hand to a 3D mousetracker
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
viz.link(mouseTracker,hand)

viz.mouse(viz.OFF)													# Disable mouse navigation

# Add a box model and set its position
basketball = viz.addChild('basketball.osgb')
basketball.setPosition([0,2,1.5])

link = None 														# The handle to the link object
													
def grabBall():
	object = viz.pick() 											# Command detects which object the mouse is currently over and returns it
	if object == basketball:										# Check to see if object is basketball
		print "You've clicked on the basketball"
		global link
		link = viz.grab( hand, basketball ) 						# Use hand to grab basketball
		glove.getSensorRawAll()
	else:
		print "This is not a basketball"
		
def releaseBall():
	global link
	link.remove()
	print "You have released the ball"
	link = None


if glove.getSensorRawAll > 2300:
	print "hi there"
	grabBall

#vizact.onmousedown(viz.MOUSEBUTTON_LEFT,grabBall)					# When left mouse button is clicked, go to pickBall function
vizact.onmouseup(viz.MOUSEBUTTON_LEFT,releaseBall)