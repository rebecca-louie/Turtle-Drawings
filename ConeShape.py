import turtle
#Draw cone-ish shape
#############################
# Author  : Rebecca 
# Date 	  : Feb 6th 2018
# Function: Experimenting with turtle module
# Usage   : python ConeShape.py
#############################
mega=turtle.Turtle()
mega.speed(1000) 
for time in range(0,180,10):
	mega.goto(0+time, 200+time)
	mega.right(30)
	mega.forward(57)
	mega.home()
#Draws left side
for time in range(0,180,10):
	mega.goto(0-time,200+time)
	mega.right(-210)
	mega.forward(57)
	mega.home()
for time in range(0,180,10):
	mega.goto(0+time, -200-time)
	mega.right(30)
	mega.forward(57)
	mega.home()
#Draws left side
for time in range(0,180,10):
	mega.goto(0-time,-200-time)
	mega.right(-210)
	mega.forward(57)
	mega.home()
turtle.exitonclick()
