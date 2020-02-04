import viz
import vizact
import viztracker

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.addChild('ground.osgb')
viz.clearcolor(viz.GRAY)

#Add the object that will do the grabbing
hand = viz.addChild('white_ball.wrl')

#link the hand to a 3D mousetracker
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
viz.link(mouseTracker,hand)

##turn off mouse navigation and hide cursor
viz.mouse(viz.OFF)
#viz.mouse.setVisible(viz.OFF)

#Add the object that the marker will grab
ball = viz.addChild( 'basketball.osgb',pos=[0.5,1.8,2.5],scale=[2,2,2])

link = None #The handle to the link object
def grabBall():
	global link
	link = viz.grab( hand, ball )

def releaseBall():
	global link
	link.remove()
	link = None
	
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,grabBall)
vizact.onmouseup(viz.MOUSEBUTTON_LEFT,releaseBall)