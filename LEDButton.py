import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(24,GPIO.OUT)
while True: 
  if GPIO.input(23) == True:
   print "Air LED on"
   GPIO.output(18,GPIO.HIGH)
   time.sleep(5)
   print "Air LED off"
   GPIO.output(18,GPIO.LOW)
  elif GPIO.input(19) == True:
   print "Pool LED on"
   GPIO.output(24,GPIO.HIGH)
   time.sleep(5)
   print "Pool LED off"
   GPIO.output(24,GPIO.LOW)
