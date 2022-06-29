from turtle import *

def hilbert_b(level, angle, step):
    if level == 0:
        return

    right(angle)
    hilbert_b(level - 1, -angle, step)

    forward(step)
    left(angle)
    hilbert_b(level - 1, angle, step)

    forward(step)
    hilbert_b(level - 1, angle, step)

    left(angle)
    forward(step)
    hilbert_b(level - 1, -angle, step)
    right(angle)

level = 2
size = 400
penup()
goto(-size / 2.0, size / 2.0)
pendown()

hilbert_b(level, 90, size / (2 ** level - 1))
done()
