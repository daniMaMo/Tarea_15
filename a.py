from turtle import *


def hilbert_a(level, angle, step):
    if level == 0:
        return

    right(angle)
    hilbert_a(level - 1, -angle, step)

    forward(step)
    if level != 1:
        left(angle)
    hilbert_a(level - 1, angle, step)
    left(angle)

    if level != 1:
        right(angle)
    forward(step)
    hilbert_a(level - 1, angle, step)

    left(angle)
    forward(step)
    hilbert_a(level - 1, -angle, step)
    right(angle)


level = 2
size = 200
penup()
goto(size / 2.0, size / 2.0)
pendown()

right(90)
hilbert_a(level, 90, size / (2 ** level - 1))
done()
