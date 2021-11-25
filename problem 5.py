#Idris Adeyemi
#11/14/21
#problem 5, the intention of this code is to provide a certain image as its end run product

import turtle


def drawsquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.hideturtle()


wn = turtle.Screen()

smith = turtle.Turtle()
smith.color("green")

size = 20

for i in range(5):
    drawsquare(smith, size)
    size = size + 20
    smith.penup()
    smith.goto(smith.pos() + (-10, -10))
    smith.pendown()

wn.exitonclick()
