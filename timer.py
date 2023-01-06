from gpiozero import AngularServo
import time
from tkinter import*
import threading

#Motor Variables
servo1 = AngularServo(18, min_pulse_width = 0.0006, max_pulse_width = 0.0024)
servo2 = AngularServo(17, min_pulse_width = 0.0006, max_pulse_width = 0.0024)



seconds = 27000  #Change input, Clock min timer 


			
	
def clock():
	global seconds,sec, mins, hrs
	
	
	if seconds > (43200): #Divide toatal time by 2, for am pm 
		am_pm = "PM"
	else:
		am_pm = "AM"
	
	
	if seconds == 86400: #If 24hr met, reset clock
		seconds = 0
		clock()
				
	else:
		sec = seconds % 60
		mins = int(seconds / 60) % 60 
		hrs = int(seconds / 3600)
		my_label.config(text= (f"{hrs:02}:{mins:02}:{sec:02} {am_pm}"))
		seconds += 10
		my_label.after(100, clock) # Change how fast clock ticks, miliseconds



def trackState ():
	global seconds,sec, mins, hrs, servo1, servo2
	
	""" Input I/O times here, in seconds 24hr clock """
	
	onHr = [29000, 27010]  #8am, 10s
	offHr = [28000]		#9am
	i = 0
	
	while True:
		if i == 15:
			Output.delete("1.0" , "end") #Deleting output box
			i = 0
		
		elif (seconds in onHr) or (seconds in offHr):
			Output.insert(END, " ! It's Operation time ! " + "(" + f"{hrs:02}:{mins:02}:{sec:02}" + ")" + "\n")
			
			#Flips switch up
			if(seconds in onHr):
				servo1.angle = -30
				servo2.angle = 30
				time.sleep(1)		
				servo1.angle = 30
			
			
			
			#Flips switch down
			elif (seconds in offHr):	
				servo1.angle = 30
				servo2.angle = -30
				
				time.sleep(1)
				
				servo2.angle = 30
		

			i += 1
			time.sleep(.1)
		
		else:
			Output.insert(END, "Not Operation Time " + "(" + f"{hrs:02}:{mins:02}:{sec:02}" + ")" + "\n" )
			i += 1
			time.sleep(.1)
			
	
	
		
""" tkinter canvas """

root = Tk()
root.title('Switch Clock')
root.iconbitmap() #Change top left icon here
root.geometry("600x400")
root.configure(background = "#1b2834" )

my_label = Label(root, pady=10, text = "", font = ("Helvetica", 48), fg= "white", bg="#1b2834")
my_label.pack(pady=20)

Output = Text(root, height = 15, width = 50, bg = "#1b2834", fg = "White" )
Output.pack()

""" Utilizing threading """

t1 = threading.Thread(target = clock)
t1.start()

t2 = threading.Thread(target = trackState)
t2.start()

root.mainloop()

