# how to record the screen just import these packages 
import cv2 			# opencv
import numpy as nu
import pyautogui			# auto Graphical User Interface 

#Screen details(Size and Quality) 
screen_size=(1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# output file where video saves
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))


while True:
	image = pyautogui.screenshot()	
	frame = nu.array(image)
	frame= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	out.write(frame)

	cv2.imshow("show that", frame)

	if cv2.waitKey(1) == ord("q"):
		break
