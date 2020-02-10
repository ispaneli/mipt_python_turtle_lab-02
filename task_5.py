import turtle
import time


def draw_cubs(num :'число квадратов, int, >0'):
    for i in range(1, num + 1):
        for j in range(4):
            turtle.forward(12 * i)
            turtle.left(90)

        turtle.penup()
        turtle.goto(-6 * i, -6 * i)
        turtle.pendown()


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_cubs(10)
    time.sleep(1)
