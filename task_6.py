import turtle
import time

if __name__ == '__main__':
    turtle.shape('turtle')

    time.sleep(1)

    n = int(input('Введите параметр n для паука (0 < n < 360): '))
    angle = 360 / n

    for i in range(n):
        turtle.forward(100)
        turtle.stamp()
        turtle.left(angle)
        turtle.goto(0, 0)

    time.sleep(1)
