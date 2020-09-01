import turtle

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    hello()

def hello():
    t.fillcolor('red')
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

t = turtle.Turtle()
t.shape("turtle")

t.pencolor("red")
t.pensize(5)

s = turtle.Screen()
s.onscreenclick(drawit)

turtle.done()
