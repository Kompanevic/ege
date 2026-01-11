from turtle import *
k = 15
tracer(0)
left(90)
for i in range(4):
    forward(5*k)
    right(90)
    forward(7*k)
    right(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3)
done()