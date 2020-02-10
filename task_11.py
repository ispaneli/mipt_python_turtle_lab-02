import turtle
import time


def draw_butterfly(num: 'длина крыла, int, >0'):
    for i in range(num):
        draw_circle(i, 'left')
        draw_circle(i, 'right')


def draw_circle(num: 'int, >=0', side: 'str, left or right'):
    if side != 'left' and side != 'right':
        return Exception('Неверно указан параметр "side"!')
    else:
        for i in range(72):
            turtle.forward(2 + num)
            if side == 'left':
                turtle.left(5)
            else:
                turtle.right(5)


if __name__ == '__main__':
    turtle.shape('turtle')
    turtle.left(90)
    time.sleep(1)

    draw_butterfly(2)
    time.sleep(1)
