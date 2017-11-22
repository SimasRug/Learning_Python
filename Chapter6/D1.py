import turtle
import random

tur = turtle.Turtle()
tur.color('red')
tur.pensize(5)
tur.speed(10)

window = turtle.Screen()
window.bgcolor('black')

def ff(range):
    return random.randrange(range)


def angle():
    ff = ff(3)
    if(ff == 0):
        tur.right(90)
    elif(ff == 1):
        tur.left(90)
    elif (ff ==2):
        tur.left(0)

def movement(direction):
    # tur.forward(50)
    if(direction == 0):
        tur.forward(50)
    else:
        tur.backward(50)


def checkWall():
    xmax = (window.window_width()/2)-100
    xmin = (-window.window_width()/2)+100
    ymax = (window.window_height()/2)-100
    ymin = (-window.window_height()/2)+100
    turtleX = tur.xcor()
    turtleY = tur.ycor()
    print( tur.heading()) #fix this later
    if(turtleX >= xmax):
        # tur.left(180)
        tur.setposition(xmax, turtleY)
    if(turtleX <= xmin):
        #  tur.right(180)
        tur.setposition(xmin, turtleY)
    if(turtleY >= ymax):
        #  tur.left(180)
        tur.setposition(turtleX, ymax)
    if(turtleY <= ymin):
        #  tur.right(180)
        tur.setposition(turtleX, ymin)


def angle():
    angle = ff(3)
    if(angle == 0):
        tur.right(90)
    elif(angle == 1):
        tur.left(90)
    elif(angle ==2):
        tur.left(0)

while True:
    # movement(ff(2))
    tur.forward(50)
    angle()
    checkWall()
    
    


# def isInScreen(window, t):
#     xmin = (-window.window_width()/2)+50
#     xmax = (window.window_width()/2)-50
#     ymin = (-window.window_height()/2)+50
#     ymax = (window.window_height()/2)-50

#     turtleX = t.xcor()
#     turtleY = t.ycor()

#     if (turtleX < xmin or turtleX > xmax):
#         t.backward(50)
#         # return False 
#     if(turtleY < ymin or turtleY > ymax):
#         t.backward(50)
#         # return False

#     return True

# while isInScreen(window, t):
#     t.fd(50)
#     coin = random.randrange(2)
#     if coin == 0:
#         t.left(90)
#     elif coin == 1:
#         t.right(90)

# turtle.mainloop()
turtle.exitonclick()