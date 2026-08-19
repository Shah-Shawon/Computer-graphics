import turtle

screen = turtle.Screen()
screen.title("2D Translation")
screen.setup(1000,800)

t = turtle.Turtle()

t.penup()
t.goto(-400,0)
t.pendown()
t.goto(400,0)
t.write(" X")

t.penup()
t.goto(0,-350)
t.pendown()
t.goto(0,350)
t.write(" Y")


x = [2,4,3,2]
y = [2,2,4,2]

scale = 50

tx = 3
ty = 2

def draw(x, y):

    t.penup()
    t.goto(x[0]*scale,y[0]*scale)
    t.pendown()

    for i in range(1, len(x)):
        t.goto(x[i]*scale, y[i]*scale)

t.color("blue")
draw(x,y)

t.penup()
t.goto(x[2]*scale,y[2]*scale+15)
t.write("original",align="center",font=("Arial",11,"bold"))

new_x = []
new_y = []

for i in range(len(x)):
    new_x.append(x[i] + tx)
    new_y.append(y[i] + ty)

t.color("red")
draw(new_x,new_y)

t.penup()
t.goto(new_x[2]*scale,new_y[2]*scale +15)
t.write("Translated",align="center",font=("Arial",11,"bold"))

t.hideturtle()
turtle.done()