import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.Board)
nums = [29,31,33,35]
vals = [False,False,False,False]
output = 0
for i in range(0,3):
    vals[i] = GPIO.input(nums[i])
    if(vals[i])
        output += 1
print(output)
