def add10(n):
    n = n + 10
    return n



import turtle
def DrawRectangle(Anyturtle, l, w):
    Anyturtle.color('purple')
    for i in range (2):
        Anyturtle.fd(l)
        Anyturtle.rt(90)
        Anyturtle.fd(w)
        Anyturtle.rt(90)



def DrawPoly(Anyturtle, n):
    Anyturtle.color('green')
    theta = 360 / n
    if n > 20:
        for i in range(n):
            Anyturtle.fd(10)
            Anyturtle.lt(theta)
    else:
        for i in range(n):
            Anyturtle.fd(50)
            Anyturtle.lt(theta)
