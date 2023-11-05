from turtle import *
bgcolor('black')
speed(0)
hideturtle()

for i in range(150):
    color('white')
    circle(i)
    color('cyan')
    circle(i*0.8)
    color('purple')
    circle(i*0.6)
    color('purple')
    circle(i*0.55)
    color('purple')
    circle(i*0.5)
    right(3)
    forward(3)

for i in range(150):
    color('white')
    circle(i)
    color('cyan')
    circle(i*0.8)
    color('purple')
    circle(i*0.6)
    color('purple')
    circle(i*0.55)
    color('purple')
    circle(i*0.5)
    left(3)
    forward(3)

done()
