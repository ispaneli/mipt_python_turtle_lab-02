import turtle
import time

if __name__ == '__main__':
    turtle.shape('turtle')

    time.sleep(1)

    for i in range(180):
        turtle.forward(2)
        turtle.left(2)

    time.sleep(1)
