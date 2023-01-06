from gpiozero import AngularServo
import tkinter as tk
from tkinter import *
import time, os

#Motor Variables
servo1 = AngularServo(18, min_pulse_width = 0.0006, max_pulse_width = 0.0024)
servo2 = AngularServo(17, min_pulse_width = 0.0006, max_pulse_width = 0.0024)


#Set times, when switch flipped
onHr = ["09"]
offHr = ["20"]
i = 0


user1 = input("Type manual or auto: ")

while (1):
	
	while(user1 == "auto"):
		time_object = time.localtime()
		local_time = time.strftime("%a " "%H" " %s" " %M", time_object )
		
		#if (local_time[4:6] in onHr and local_time[15:17] == "00" and local_time[18:20] == "00"): # hrs - sec - min
		if (i == 0):
			servo1.angle = -30
			servo2.angle = 30
			
			time.sleep(1)
			
			servo1.angle = 30
			
			
			
			print("Turned on")
			i += 1
			time.sleep(1)
			break
			
		#elif (local_time[4:6] in offHr and local_time[15:17] == "00" and local_time[18:20] == "00"):
		elif (i == 1):
			servo1.angle = 30
			servo2.angle = -30
			
			time.sleep(1)
			
			servo2.angle = 30
			
			print("Turned off")
			i = 0
			time.sleep(1)
			break
			
				
		else:
			print("Not Operation time....")
			time.sleep(1)
		
		
		
			
		
		
				 
		


	while(user1 == "manual"):
		
		user2 = input("Type: on - off - change mode \n")
		if (user2 == "change mode"):
			user1 = "auto"
			break
			


		#Flips switch up
		if(user2 == "on"):
			servo1.angle = -30
			servo2.angle = 30
			time.sleep(1)		
			servo1.angle = 30
			i = 3
		
		
		
		elif (user2 == "off"):	
			servo1.angle = 30
			servo2.angle = -30
			
			time.sleep(1)
			
			servo2.angle = 30
			i = 3	 
		else:
			print("Wrong input")
		
		 

