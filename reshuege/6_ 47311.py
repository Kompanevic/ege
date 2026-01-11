from turtle import *
k = 15
tracer(0)
left(90)
for i in range(4):
    forward(12*k)
    right(150)
    forward(12*k)
    right(30)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3)
done()