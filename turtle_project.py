import turtle

def draw_square(draw, the_shape, the_color, size, the_bgcolor=None):
    draw.shape(the_shape)
    if the_bgcolor is None:
        draw.color(the_color)
    else:
        draw.color(the_color, the_bgcolor)
    if the_bgcolor is not None:
        draw.begin_fill()
    for i in range(4):
        draw.forward(size)
        draw.right(90)
    draw.end_fill()

def draw_circle(draw, the_shape, the_color, size, the_bgcolor=None):
    draw.shape(the_shape)
    if the_bgcolor is None:
        draw.color(the_color)
    else:
        draw.color(the_color, the_bgcolor)
    if the_bgcolor is not None:
        draw.begin_fill()
    draw.circle(size)
    draw.end_fill()

def draw_triangle(draw, the_shape, the_color, size, the_bgcolor=None):
    draw.shape(the_shape)
    if the_bgcolor is None:
        draw.color(the_color)
    else:
        draw.color(the_color, the_bgcolor)
    if the_bgcolor is not None:
        draw.begin_fill()
    for i in range(3):
        draw.forward(size)
        draw.left(120)
    draw.end_fill()

def draw_flower(draw, the_shape, the_color, size, the_bgcolor=None):
    draw.shape(the_shape)
    if the_bgcolor is None:
        draw.color(the_color)
    else:
        draw.color(the_color, the_bgcolor)
    if the_bgcolor is not None:
        draw.begin_fill()
    for i in range(36):
        draw.left(35)
        draw.forward(size)
        draw.right(35)
        draw.forward(size)
        draw.right(145)
        draw.forward(size)
        draw.right(35)
        draw.forward(size)
        draw.right(10)
    draw.seth(270)
    draw.forward(size*4)
    draw.end_fill()
window = turtle.Screen()
window.bgcolor("#000")

brad = turtle.Turtle()
brad.speed(50)

#draw_square(brad, "turtle", "#FFF", 100, "red")
#draw_circle(brad, "turtle", "#FFF", 100, "red")
#draw_triangle(brad, "turtle", "#FFF", 100, "red")
draw_flower(brad, "turtle", "#FFF", 100, "red")
window.exitonclick()
