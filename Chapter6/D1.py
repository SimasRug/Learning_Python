import turtle
import random

tur = turtle.Turtle()
# tur1 = turtle.Turtle()
# tur2 = turtle.Turtle()
tur.color('grey')
# tur1.color('white')
# tur2.color('red')
tur.pensize(5)
# tur1.pensize(5)
# tur2.pensize(5)
tur.speed(0)
# tur1.speed(0)
# tur2.speed(0)
turtle.setup(800,800)
window = turtle.Screen()
window.bgcolor('black')

def ff(range):
    return random.randrange(range)

def checkWall(t):
    xmax = (window.window_width()/2)-100
    xmin = -xmax#(-window.window_width()/2)+100
    ymax = (window.window_height()/2)-100
    ymin = (-window.window_height()/2)+100
    turtleX = t.xcor()
    turtleY = t.ycor()
    # print( tur.heading()) #fix this later
    if(turtleX >= xmax):
        t.setheading(180)
        t.setposition(xmax, turtleY)
        # angle(t)
    if(turtleX <= xmin):
        t.setheading(0)
        # angle(t)
        t.setposition(xmin, turtleY)
    if(turtleY >= ymax):
        t.setheading(270)
        # angle(t)
        t.setposition(turtleX, ymax)
    if(turtleY <= ymin):
        t.setheading(90)
        # angle(t)
        t.setposition(turtleX, ymin)


def angle(t):
    angle = ff(3)
    if(angle == 0):
        t.right(90)
    elif(angle == 1):
        t.left(90)
    elif(angle ==2):
        t.left(0)

while True:
    tur.forward(50)
    # tur1.forward(50)
    # tur2.forward(50)
    angle(tur)
    # angle(tur1)
    # angle(tur2)
    checkWall(tur)
    # checkWall(tur1)
    # checkWall(tur2)
    
turtle.exitonclick()