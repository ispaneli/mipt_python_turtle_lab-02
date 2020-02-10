import turtle
import time
from math import *


def draw_encapsulation(num: 'кол-во фигур, int, >0'):
    for i in range(num):
        turtle.penup()
        turtle.goto(get_radius(3 + i), 0)
        turtle.pendown()

        draw_correct_figure(3 + i)


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

    draw_encapsulation(2)
    time.sleep(1)
