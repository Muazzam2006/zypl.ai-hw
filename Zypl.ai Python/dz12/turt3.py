from turtle import Turtle, Screen
import math

h = Turtle()
s = Screen()
h.shape("turtle")
h.color("turquoise")

i = 0
n = 300
while i < 6:
    h.fd(n)
    h.left(90)
    h.fd(n)
    h.left(135)
    h.fd(math.sqrt(2 * (n**2)))
    h.left(135)

    h.up()
    h.fd(30)
    h.left(90)
    h.fd(12)
    h.right(90)
    h.pendown()

    i += 1
    n -= 50

s.exitonclick()
