from turtle import Turtle, Screen
h = Turtle()
s = Screen()
h.shape("turtle")
h.color("turquoise")

i = 0
n = 300
while i < 6:
    for j in range(4):
        h.fd(n)
        h.left(90)

    h.up()
    h.fd(25)
    h.left(90)
    h.fd(25)
    h.right(90)
    h.pendown()

    i += 1
    n -= 50

s.exitonclick()
