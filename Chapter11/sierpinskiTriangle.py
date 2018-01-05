import turtle
import math

def createTriangleShape(coords):
    turtle.penup()
    turtle.begin_poly()
    turtle.setposition(coords[0])
    turtle.setposition(coords[1])
    turtle.setposition(coords[2])
    turtle.setposition(coords[0])

    tri_shape = turtle.get_poly()
    turtle.register_shape('my_triangle', tri_shape)



def triangleHeight(side):
    return math.sqrt(3) / 2 * side


def getLeftTrianglePosition(position, side):
    return(position[0] - side / 4, position[1] - triangleHeight(side) / 4)

def getRightTrianglePosition(position, side):
    return (position[0] + side / 4, position[1] - triangleHeight(side) / 4)

def getTopTrianglePosition(position, side):
    return (position[0], position[1] + triangleHeight(side) / 4)


def drawSierpimskyTriangle(t, len_side, levels):

    if levels == 0:
        t.color('black')
        t.showturtle()
        t.stamp()

        return

    stretch_width, stretch_length, outline = t.turtlesize()
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    left_triangle_position = getLeftTrianglePosition(t.position(), len_side)

    right_triangle_position = getRightTrianglePosition(t.position(), len_side)

    top_triangle_position = getTopTrianglePosition(t.position(), len_side)

    t.setposition(left_triangle_position)
    drawSierpimskyTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    t.setposition(right_triangle_position)
    drawSierpimskyTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    t.setposition(top_triangle_position)
    drawSierpimskyTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)





# --- main

turtle.setup(800,600)

the_turtle = turtle.getturtle()

the_turtle.penup()
the_turtle.hideturtle()

num_levels = 2

coords = ((-240, -150),(240, -150),(0, 266))
createTriangleShape(coords)
len_side = 480

the_turtle.shape('my_triangle')
the_turtle.setposition(0, -50)
the_turtle.setheading(90)

drawSierpimskyTriangle(the_turtle, len_side, num_levels)
the_turtle.hideturtle()

turtle.exitonclick()