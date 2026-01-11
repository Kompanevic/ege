from turtle import *
tracer(0)
left(90)
k = 10
forward(5*k)
right(60)
for i in range(6):
    forward(23*k)
    right(45)
    forward(17*k)
    right(135)
left(90)
forward(7*k)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3)
done()