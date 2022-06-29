from turtle import *

def hilbert_c(level, angle, step):

    def step1(level):
        if level != 0:
            left(angle)
            step2(level - 1)
            forward(step)
            right(angle)
            step1(level - 1)
            forward(step)
            step1(level - 1)
            right(angle)
            forward(step)
            step2(level - 1)
            left(angle)

    def step2(level):
        if level != 0:
            right(angle)
            step1(level - 1)
            forward(step)
            left(angle)
            step2(level - 1)
            forward(step)
            step2(level - 1)
            left(angle)
            forward(step)
            step1(level - 1)
            right(angle)

    left(angle)
    step2(level)

level = 2
size = 200
penup()
goto(size / 2.0, -size / 2.0)
pendown()

left(90)
hilbert_c(level, 90, size / (2 ** level - 1))
done()
