import viz
import vizact
import hand


viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Identify the data glove's port.
PORT_5DT_USB = 0

#Add the 5DT sensor
sensor = viz.addSensor('5dt.dls')

#Create a hand object from the data glove
glove = hand.add(sensor,hand.GLOVE_5DT)

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

gestureText = viz.addText( '', viz.SCREEN )
gestureText.setPosition(0.5,0.1)
gestureText.alignment(viz.ALIGN_CENTER)

def getGesture():
    gesture = int(sensor.get()[-1])
    gestureText.message(gestureName[gesture])
    if gesture == 0:
        print "closed fist"
    if gesture == 15:
        print "open hand"
vizact.ontimer(0, getGesture)