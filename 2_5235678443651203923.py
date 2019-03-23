import turtle
from builtins import range

ob = turtle.Turtle()

for i in range(3):
    ob.pencolor("red")
    ob.fd(100)
    ob.lt(120)

ob.done()
ob.mainloop()
