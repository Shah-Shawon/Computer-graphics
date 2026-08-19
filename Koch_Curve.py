import turtle

screen = turtle.Screen()
screen.title("Koch graph")
screen.setup(1000,700)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)



def koch(length,level):
    if level ==0:
        t.forward(length)
    else:
        length = length / 3

        koch(length, level-1)
        t.left(60)

        koch(length, level-1)
        t.right(120)

        koch(length, level-1)
        t.left(60)

        koch(length, level-1)

t.penup()
t.goto(-300,100)
for _ in range(3):
    t.pendown()
    koch(500,4)
    t.right(120)


t.hideturtle()
turtle.done()

