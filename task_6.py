import turtle
import time


def draw_spider(num: 'кол-во ног, int, >0'):
    angle = 360 / num

    for i in range(num):
        turtle.forward(100)
        turtle.stamp()
        turtle.left(angle)
        turtle.goto(0, 0)


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_spider(12)
    time.sleep(1)
