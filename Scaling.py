import turtle

screen = turtle.Screen()
screen.setup(1000,700)
screen.title("Bresenham curve")

t= turtle.Turtle()
t.speed(3)
t.pensize(2)

t.penup()
t.goto(-450,0)
t.pendown()
t.goto(450,0)
t.write(" X")

t.penup()
t.goto(0,-350)
t.pendown()
t.goto(0,350)
t.write(" Y")

x = [2, 4, 3, 2]
y = [2, 2, 4, 2]

scale = 25

sx = 2
sy = 3


def draw(x, y):

    t.penup()
    t.goto(x[0]*scale, y[0]*scale)
    t.pendown()

    for i in range(1, len(x)):
        t.goto(x[i] * scale, y[i] * scale)

t.color("Blue")
draw(x, y)

t.penup()
t.goto(x[2] * scale, y[2] * scale)
t.write("Original", align = "center", font = ("Arial", 12, "bold"))

x_new = []
y_new = []

for i in range(len(x)):
    x_new.append(x[i] * sx)
    y_new.append(y[i] * sy)

t.color("red")
draw(x_new, y_new)

t.penup()
t.goto(x_new[2] * scale, y_new[2] * scale)
t.write("Scaled", align = "center", font = ("Arial", 12, "bold"))

t.hideturtle()
turtle.done()