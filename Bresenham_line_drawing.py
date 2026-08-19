import turtle
import math

screen = turtle.Screen()
screen.title("Bresenham Line drawing")
screen.setup(1000,800)

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

t.penup()
t.goto(-550,0)
t.pendown()
t.goto(550,0)
t.write(" X",font=("Arial",12,"bold"))

t.penup()
t.goto(0,-400)
t.pendown()
t.goto(0,400)
t.write(" Y",font=("Arial",12,"bold"))

x1,y1,x2,y2 = 20,10,30,18

dx = abs(x2 - x1)
dy = abs(y2 - y1)

p = 2*dy - dx

x_points = []
y_points = []

x = x1
y = y1

x_points.append(x)
y_points.append(y)

while x < x2:
    if p< 0:

        x = x+1
        y=y

        p = p+2*dy
    else:
        x = x+1
        y = y+1

        p = p + 2 * dy - 2 * dx

    x_points.append(x)
    y_points.append(y)

scale = 20

t.color("blue")

for i in range(len(x_points)):
    x = x_points[i]*scale
    y = y_points[i]*scale

    if i==0:
        t.penup()
        t.goto(x,y)
        t.dot(8)
        t.pendown()
    else:
        t.goto(x,y)
        t.dot(8)

    t.write(
            f" ({x_points[i]}, {y_points[i]})",
            font=("Arial", 10, "normal")
        )

    print(f"{x_points[i]},{y_points[i]}")



t.hideturtle()
turtle.done()