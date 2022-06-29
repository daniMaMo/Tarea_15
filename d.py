from turtle import *

def hilbert_d(level, angle, step):
    if level == 0:
        return

    left(angle)
    hilbert_d(level - 1, -angle, step)
    forward(step)

    if level !=1:
        right(angle)

    hilbert_d(level - 1, angle, step)

    if level !=1:
        left(angle)

    right(angle)
    forward(step)

    hilbert_d(level - 1, angle, step)
    right(angle)
    forward(step)

    hilbert_d(level - 1, -angle, step)
    left(angle)

level = 2
size = 200
penup()
goto(-size / 2.0, -size / 2.0)
pendown()

hilbert_d(level, 90, size / (2 ** level - 1))
done()
