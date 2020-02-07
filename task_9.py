import turtle
import time
from math import *


def draw_correct_figure(size):
    angle = (size - 2) * 180 / size
    a = 60 * size / 4

    turtle.left(180 - angle / 2)

    for i in range(size):
        turtle.forward(a)
        turtle.left(180 - angle)

    turtle.right(180 - angle / 2)


def get_radius(size):
    a = 60 * size / 4
    return a / (2 * sin(radians(360 / (2 * size))))


if __name__ == '__main__':
    turtle.shape('turtle')

    time.sleep(1)

    for i in range(3, 13):
        turtle.penup()
        turtle.goto(get_radius(i), 0)
        turtle.pendown()

        draw_correct_figure(i)

    time.sleep(3)
