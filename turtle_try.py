import turtle

t = turtle.Turtle()
t.speed(3)

t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300,0)
t.write(" X")

t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)
t.write(" Y")

turtle.done()