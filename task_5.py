import turtle
import time

if __name__ == '__main__':
    turtle.shape('turtle')

    time.sleep(1)

    for i in range(1, 11):
        for j in range(4):
            turtle.forward(12 * i)
            turtle.left(90)

        turtle.penup()
        turtle.goto(-6 * i, -6 * i)
        turtle.pendown()

    time.sleep(1)
