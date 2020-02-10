import turtle
import time


def draw_spring(num: 'длина пружины, int, >0'):
    for i in range(num - 1):
        draw_arc()
        draw_hook()
    else:
        draw_arc()


def draw_arc():
    for i in range(45):
        turtle.forward(3)
        turtle.right(4)


def draw_hook():
    for i in range(22):
        turtle.forward(1)
        turtle.right(8)
    else:
        turtle.right(4)


if __name__ == '__main__':
    turtle.shape('turtle')
    turtle.left(90)
    time.sleep(1)

    draw_spring(6)
    time.sleep(1)
