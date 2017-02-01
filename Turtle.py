import turtle
"""Create a Turtle Program that will draw a 3-dimensional cube"""
def cube(Anyturtle):
    Anyturtle.color('red')
    for i in range(4):
        Anyturtle.fd(100)
        Anyturtle.rt(90)
    Anyturtle.up()
    x1 = Anyturtle.xcor()
    y1 = Anyturtle.ycor()
    for i in range(2):
        Anyturtle.fd(100)
        Anyturtle.rt(90)
    x3 = Anyturtle.xcor()
    y3 = Anyturtle.ycor()
    for i in range (2):
        Anyturtle.fd(100)
        Anyturtle.rt(90)
    Anyturtle.lt(90)
    Anyturtle.fd(50)
    Anyturtle.rt(90)
    Anyturtle.fd(50)
    Anyturtle.down()
    Anyturtle.fd(100)
    x2 = Anyturtle.xcor()
    y2 = Anyturtle.ycor()
    Anyturtle.rt(90)
    Anyturtle.fd(100)
    Anyturtle.bk(100)
    Anyturtle.lt(90)
    Anyturtle.bk(100)
    Anyturtle.goto(x1,y1)
    Anyturtle.fd(100)
    Anyturtle.goto(x2, y2)
    Anyturtle.rt(90)
    Anyturtle.fd(100)
    Anyturtle.goto(x3,y3)
sam = turtle.Turtle()
cube(sam)
input()



"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
from myfile import DrawRectangle
steve = turtle.Turtle()
#DrawRectangle(steve, 100, 50)
