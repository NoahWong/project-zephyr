import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.Board)
GPIO.setup(15,GPIO.OUT) #Right Drive
GPIO.setup(16,GPIO.OUT) #Left Drive
GPIO.setup(36,GPIO.OUT) #Enabler
GPIO.setup(38,GPIO.OUT) #Right Run
GPIO.setup(40,GPIO.OUT) #Left Run
#Drive Motors
GPIO.output(15, True)
GPIO.outout(16, True)
#Rudder Motor
GPIO.output(36, False)
GPIO.output(38, False)
GPIO.output(40, False)
minutes = 60
turnStart = 0
straightStart = 10
moveTime = 2
	for num in range(1,(minutes*60)):
		if num % 60 == turnStart #Start turning rudder left
                        GPIO.output(36, True)
                        GPIO.output(38, True)
                        GPIO.output(40, False)
                elif num % 60 == (turn Start + moveTime) #Stop turning rudder left
                        GPIO.output(36, False)
                        GPIO.output(38, False)
                        GPIO.output(40, False)
                elif num % 60 == straightStart #Start restraightening rudder
                        GPIO.output(36, True)
                        GPIO.output(38, False)
                        GPIO.output(40, True)
                elif num % 60 == (straightStart + moveTime) #Stop restraightening rudder
                        GPIO.output(36, False)
                        GPIO.output(38, False)
                        GPIO.output(40, False)
		time.sleep(1)
GPIO.cleanup()
