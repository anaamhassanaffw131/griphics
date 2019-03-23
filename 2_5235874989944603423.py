import turtle

ob = turtle.Turtle()

def draw(c, x, y):
    ob.pencolor(c)
    ob.pensize(width=10)
    ob.circle(60)
    ob.pu()
    ob.goto(x, y)
    ob.pd()


draw("red", 120, -1)
draw("yellow", 180, 90)
draw("green", 65, 90)
draw("blue", -59, 90)
draw("black", 0, 0)

turtle.done()