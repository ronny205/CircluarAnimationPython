# importing turtle
import turtle

# initialise the turtle instance
Rohan = turtle.Turtle()

#creating animation
# changes speed of turtle
Rohan.speed(0)

# hiding turtle
Rohan.hideturtle()

# changing background color
Rohan.getscreen().bgcolor("green")

# color of the animation
Rohan.color("orange")

for i in range(8000):
	
	# drawing circle using circle function
	# by passing radius i
	Rohan.circle(i)

	# changing turtle face by 5 degree from it's
	# previous position after drawing a circle
	Rohan._rotate(1)