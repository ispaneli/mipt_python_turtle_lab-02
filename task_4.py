import turtle
import time

if __name__ == '__main__':
    turtle.shape('turtle')

    time.sleep(1)

    for i in range(360):
        turtle.forward(2)
        turtle.left(1)

    time.sleep(1)
