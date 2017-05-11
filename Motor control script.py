import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.Board)
n = 22
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
burst = True
#Emergency Button
GPIO.setup(n,GPIO.IN)
for num in range(1, takeoff) #for the amount of time takeoff needs to happen
    GPIO.output(u,True)
GPIO.output(u,False) #end takeoff and begin forward motion
GPIO.output(l,True)
GPIO.output(r,True)
for num in range(1,(minutes*60)): #for the amount of time we need it to run in seconds
    if(left)
        if num % interval == turnStart #Start turning rudder left
	    GPIO.output(a, True)
            GPIO.output(b, False)
	elif num % interval == (turn Start + moveTime) #Stop turning rudder left
	    GPIO.output(a, False)
            GPIO.output(b, False)
	elif num % interval == straightStart #Start restraightening rudder from left
	    GPIO.output(a, False)
	    GPIO.output(b, True)
    else
        if num % interval == turnStart #Start turning rudder right
	    GPIO.output(a, False)
	    GPIO.output(b, True)
        elif num % interval == (turn Start + moveTime) #Stop turning rudder right
	    GPIO.output(a, False)
	    GPIO.output(b, False)
        elif num % interval == straightStart #Start restraightening rudder from right
	    GPIO.output(a, True)
	    GPIO.output(b, False)
						
    if num % interval == (straightStart + moveTime) #Stop restraightening rudder
	GPIO.output(a, False)
	GPIO.output(b, False)
	left = !left
    #Sensor recording code here
    if (GPIO.input(n)) #Emergency Shutdown
        GPIO.cleanup()
	sys.exit("Emergency Shutdown Engaged!!!")
    GPIO.output(u,burst) #Burst upward drive motor to stay aloft
    time.sleep(1)
    burst = !burst
while True:         #Blimp will circle in place
    GPIO.output(a, False)
    GPIO.output(b, False)
    GPIO.output(l, False)
    GPIO.output(r, True)
    if(GPIO.input(n)) #End-program
        GPIO.cleanup()
        sys.exit("Normal")
