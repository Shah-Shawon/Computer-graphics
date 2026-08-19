import turtle 
import math

screen = turtle.Screen()
screen.title("2D Rotation")
screen.setup(1000,800)

t = turtle.Turtle()
t.speed(3)

t.penup()
t.goto(-400,0)
t.pendown()
t.goto(400,0)
t.write(" X")

t.penup()
t.goto(0,-300)
t.pendown()
t.goto(0,300)
t.write(" Y")

x = [2,4,3,2]
y = [2,2,4,2]

scale = 50
theta = math.radians(60)

def draw(x,y):
    t.penup()
    t.goto(x[0]*scale,y[0]*scale)
    t.pendown()

    for i in range(1,len(x)):
        t.goto(x[i]*scale,y[i]*scale)

t.color("blue")
draw(x,y)

x_new = []
y_new = []

for i in range(len(x)):
    x_new.append(x[i]*math.cos(theta)-y[i]*math.sin(theta))
    y_new.append(x[i]*math.sin(theta)+y[i]*math.cos(theta))

t.color("Red")
draw(x_new,y_new)


t.hideturtle()
turtle.done()