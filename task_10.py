import turtle
import time

def draw_circle(number: 'int, >=0', side: 'str, left or right'):
    if side != 'left' and side != 'right':
        print('Неверно указаны аргументы для функции "draw_circle()!"')
        return

    for i in range(72):
        turtle.forward(2 + number)
        if side == 'left':
            turtle.left(5)
        else:
            turtle.right(5)


if __name__ == '__main__':
    turtle.shape('turtle')
    turtle.left(90)

    time.sleep(1)

    for i in range(10):
        draw_circle(i, 'left')
        draw_circle(i, 'right')

    time.sleep(3)
