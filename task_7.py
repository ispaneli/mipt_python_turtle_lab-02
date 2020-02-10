import turtle
import time


def draw_spiral(size, coef=0):
    for i in range(size):
        for j in range(1, 73):
            if j % 36 == 0:
                coef += 1
            turtle.forward(3 + coef)
            turtle.left(5)


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_spiral(10)
    time.sleep(1)
