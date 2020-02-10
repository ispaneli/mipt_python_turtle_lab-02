import turtle
import time


def draw_star(num: 'int, >0'):
    """Рисует звезду.

    :param num: число вершин звезды.
    :return: нарисованную зезду.
    """
    angle = 180 / num
    print(angle)
    turtle.left(angle)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    for i in range(num):
        turtle.left(180 - angle)
        turtle.forward(200)


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_star(11)
    time.sleep(10)
