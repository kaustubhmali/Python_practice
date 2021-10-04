# Mars Perseverance Rover - Challenge #1 - www.101computing.net/mars-perseverance-rover/
import turtle

screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)
screen.bgpic("pngs/mars-path-1.png")

# Initialise the rover...
rover = turtle.Turtle()
screen.addshape("pngs/rover.png")
rover.shape("pngs/rover.png")
rover.speed(2)

rover.color("#810000")
rover.pensize(4)
rover.penup()
rover.goto(-165, -165)
rover.pendown()

# Implement Rover Path...
rover.forward(100)
rover.left(45)
rover.forward(50)
