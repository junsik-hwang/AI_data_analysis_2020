import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(100)

def draw_star(x_pos, y_pos):
    t.penup()
    t.goto(star_garo_pos[x_pos],star_sero_pos[y_pos])
    t.pendown()
    for i in range(5):
        t.forward(15)
        t.left(72)
        t.forward(15)
        t.right(144)
        

def draw_all(x,y):
    for i in range(x):
        for j in range(y):
            draw_star(i,j)

star_garo_pos = list(range(-300, 300, 100))
star_sero_pos = list(range(300, -200, -100))
draw_all(6,5)

star_garo_pos = list(range(-250,250,100))
star_sero_pos = list(range(250,-150,-100))
draw_all(5,4)

t.hideturtle()

