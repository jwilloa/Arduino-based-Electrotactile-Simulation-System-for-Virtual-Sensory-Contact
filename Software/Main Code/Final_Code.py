####### IMPORT FUNCTIONS ###########
import viz
import vizact
import hand
import time
import viztracker

#####################################
    
####### SET WORLD VALUES ###########
viz.setMultiSample(4)
viz.fov(60)
viz.go()
viz.addChild( 'ground.osgb' )
########################### #########

                                            ########## SET PORTS ###############
PORT_5DT_USB = 0                            # Identify the data glove's port.
sensor = viz.addSensor('5dt.dls')           # Add the 5DT sensor
glove = hand.add(sensor, hand.GLOVE_5DT)    # Create a hand object from the data glove

##Place the hand in front of the user
glove.setEuler([0, -65, 10])
glove.setPosition([0, 0.8, 0])
viz.MainView.setPosition([0, 1.02, -0.5])
####################################

# Add an array with all the gesture names from the 5DT user's manual.

gestureName = ['Fist', 'Index finger point', 'Middle finger point',
               'Two finger point', 'Ring finger point', 'Ring-Index finger point',
               'Ring-middle finger point', 'Three finger point', 'Little finger point',
               'Index and little finger point', 'Little-middle finger point',
               'Not ring finger point', 'Little-ring finger point',
               'Not middle finger point', 'Not index finger point',
               'Flat hand', 'Undefined']

gestureText = viz.addText('', viz.SCREEN)
gestureText.setPosition(0.5, 0.1)
gestureText.alignment(viz.ALIGN_CENTER)

########## ADDITIONAL STUFF ###############
hand = viz.add('white_ball.wrl')  # Add the object that will do the grabbing

# Link the hand to a 3D mousetracker
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
viz.link(mouseTracker, hand)

viz.mouse(viz.OFF)  # Disable mouse navigation

# Link the hand to a 3D mousetracker
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
viz.link(mouseTracker, hand)

viz.mouse(viz.OFF)  # Disable mouse navigation

# Add a box model and set its position
basketball = viz.addChild('basketball.osgb')
basketball.setPosition([0, 1, 1.5])

link = None


def grabBall():
    gesture = int(sensor.get()[-1])
    gestureText.message(gestureName[gesture])
    object = viz.pick()                                    # Command detects which object the mouse is currently over and returns it

    if (gesture == 0) and (object == basketball):           # Check to see if object is basketball
        print
        "closed fist - gripped basketball"
      #  ser.writelines(b'T')
        global link
        link = viz.grab(hand, basketball)                   # Use hand to grab basketball
        glove.getSensorRawAll()

    else:
        print
        "This is not a basketball"
      #  ser.writelines(b'L')
        vizact.ontimer(1, releaseBall)
        vizact.ontimer(2, releaseBall)
        vizact.ontimer(3, releaseBall)
        vizact.ontimer(4, releaseBall)
        vizact.ontimer(5, releaseBall)
        vizact.ontimer(6, releaseBall)
        vizact.ontimer(7, releaseBall)
        vizact.ontimer(8, releaseBall)
        vizact.ontimer(9, releaseBall)
        vizact.ontimer(10, releaseBall)
        vizact.ontimer(11, releaseBall)
        vizact.ontimer(12, releaseBall)
        vizact.ontimer(13, releaseBall)
        vizact.ontimer(14, releaseBall)
        vizact.ontimer(15, releaseBall)
        vizact.ontimer(16, releaseBall)


def releaseBall():
    global link
    link.remove()
    print
    "open hand - released grip on basketball"
    link = None


vizact.ontimer(0, grabBall)
vizact.ontimer(15, releaseBall)

