import turtle

screen = turtle.Screen()
screen.title("DDA Algorithm")
screen.setup(1000,800)

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

t.penup()
t.goto(-450,0)
t.pendown()
t.goto(450,0)
t.write(" X",font=("Arial",12,"bold"))

t.penup()
t.goto(0,-350)
t.pendown()
t.goto(0,350)
t.write(" Y",font=("Arial",12,"bold"))

x1,y1,x2,y2 = 2,3,10,8

dx = abs(x2-x1)
dy = abs(y2-y1)

m = dy/dx

x_points = []
y_points = []

x = x1
y = y1

x_points.append(x)
y_points.append(y)

if abs(dx)>= abs(dy):
    dx = 1
    dy = m

    while x<=x2:
        x_points.append(round(x))
        y_points.append(round(y))

        x = x + dx
        y = y + dy

else:
    dy = 1
    dx = 1/m

    while y<= y2:
        x_points.append(round(x))
        y_points.append(round(y))

        x = x+dx
        y = y+dy

scale = 40

for i in range(len(x_points)):
    x = x_points[i]*scale
    y = y_points[i]*scale

    if i ==0 :
        t.penup()
        t.goto(x,y)
        t.dot(8)
        t.pendown()

    else:
        t.goto(x,y)
        t.dot(8)

    t.write(f"({x_points[i]},{y_points[i]})", font=("Arial",12,"bold"))
    print(x_points[i], y_points[i])
        


t.hideturtle()
turtle.done()
