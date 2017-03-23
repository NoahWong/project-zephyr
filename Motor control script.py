import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.Board)
e = 36
n = True
a = 38
b = 40
l = 16
r = 14
u = 12
GPIO.setup(r,GPIO.OUT) #Right Drive
GPIO.setup(r,GPIO.OUT) #Left Drive
GPIO.setup(e,GPIO.OUT) #Enabler
GPIO.setup(a,GPIO.OUT) #A
GPIO.setup(b,GPIO.OUT) #B
#Drive Motors
GPIO.output(l, False)
GPIO.outout(r, False)
#Rudder Motor
GPIO.output(e, False)
GPIO.output(a, False)
GPIO.output(b, False)
#Vertical Motors
GPIO.output(u, False)
#Time Interval
takeoff = 15 #seconds
minutes = 60 #minutes
interval = 60 #seconds
turnStart = 0 #seconds
straightStart = 10 #seconds
moveTime = 2 #seconds
left = True
for num in range(1, takeoff)
    GPIO.output(u,True)
GPIO.output(u,False)
GPIO.output(l,True)
GPIO.output(r,True)
for num in range(1,(minutes*60)):
    if(left)
        if num % interval == turnStart #Start turning rudder left
	    GPIO.output(e, True)
	    GPIO.output(a, True)
            GPIO.output(b, False)
	elif num % interval == (turn Start + moveTime) #Stop turning rudder left
	    GPIO.output(e, False)
	    GPIO.output(a, False)
            GPIO.output(b, False)
	elif num % interval == straightStart #Start restraightening rudder from left
	    GPIO.output(e, True)
	    GPIO.output(a, False)
	    GPIO.output(b, True)
    else
        if num % interval == turnStart #Start turning rudder right
	    GPIO.output(e, True)
	    GPIO.output(a, False)
	    GPIO.output(b, True)
        elif num % interval == (turn Start + moveTime) #Stop turning rudder right
	    GPIO.output(e, False)
	    GPIO.output(a, False)
	    GPIO.output(b, False)
        elif num % interval == straightStart #Start restraightening rudder from right
	    GPIO.output(e, True)
	    GPIO.output(a, True)
	    GPIO.output(b, False)
						
    if num % interval == (straightStart + moveTime) #Stop restraightening rudder
	GPIO.output(e, False)
	GPIO.output(a, False)
	GPIO.output(b, False)
	left = !left
    if (!n)
	sys.exit("Emergency Shutdown Engaged!!!")
    time.sleep(1)
GPIO.output(e, False) #Blimp will circle in place
n = False
GPIO.output(a, False)
GPIO.output(b, False)
GPIO.output(l, False)
GPIO.outout(r, True)
GPIO.cleanup()
