import turtle
import time


def draw_flower(num: 'число липестей, int, >0, %2=0'):
    """Функция рисует цветов.

    num - число лепестков.
    Условия параметра num: 1) int
                           2) 360 > num > 0
                           3) num % 2 == 0
    """
    if num % 2 != 0:
        print('kek')
        return Exception
    else:
        angle = 360 // num
        print(angle)
        for i in range(num // 2):
            draw_circle(2, 'left')
            draw_circle(2, 'right')
            turtle.left(angle)


def draw_circle(num: 'int, >=0', side: 'str, left or right'):
    if side != 'left' and side != 'right':
        return Exception
    else:
        for i in range(72):
            turtle.forward(2 + num)
            if side == 'left':
                turtle.left(5)
            else:
                turtle.right(5)


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_flower(6)
    time.sleep(1)
