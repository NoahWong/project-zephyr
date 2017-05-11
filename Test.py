import Rpi.GPIO as GPIO
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
GPIO.setup(l,GPIO.OUT) #Left Drive
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
#Emergency Button
GPIO.setup(n,GPIO.IN)

GPIO.output(u,True)
for s in range(1,10)
    sleep(1)
    if(GPIO.input(n))
        GPIO.cleanup()
        sys.exit("Emergency shutdown")
GPIO.setup(u,False)
GPIO.cleanup()
sys.exit("Normal")
