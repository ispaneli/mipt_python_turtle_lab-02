import turtle
import time


def draw_smiley_face():
    draw_circle(7, color_inside='yellow')
    _move(-45, 115)
    draw_circle(1, color_inside='blue')
    _move(45, 115)
    draw_circle(1, color_inside='blue')
    _move(0, 90)
    turtle.right(90)
    turtle.width(9)
    turtle.goto(0, 60)
    _move(-55, 75)
    draw_smile()


def _move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_smile():
    turtle.color('red')
    for i in range(90):
        turtle.forward(2)
        turtle.left(2)


def draw_circle(num: 'int, >=0', color_inside='white'):
    turtle.begin_fill()

    for i in range(90):
        turtle.forward(num)
        turtle.left(4)
    else:
        turtle.color(color_inside)
        turtle.end_fill()
        turtle.color('black')


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_smiley_face()
    time.sleep(3)
