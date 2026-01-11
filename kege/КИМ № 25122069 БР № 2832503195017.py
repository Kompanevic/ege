for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if (((x <= y) and (z <= w)) or (x == z and w)) == 0:
                    print(x,y,z,w)

x = []
for n in range(0,10000):
    s = bin(n)[2:]
    if n % 5 == 0:
        s = '5' + s
    else:
        s += s[-1:]
r = int(s,2)
f = str(r)
if len(f) and  r % 2 == 0:
    x.append(n)
    print(max(n))

from turtle import *
tracer(0)
left(90)
k = 15
for i in range(4):
    fd(20*k)
    right(90)
pu()
right(90)
fd(3*k)
left(90)
pd()
for i in range(4):
    left(90)
    fd(14*k)
pu()
fd(20*k)
pd()
for i in range(4):
    fd(6*k)
    right(90)
right(90)
pu()
fd(4*k)
left(90)
fd(4*k)
pd()
for i in range(2):
    left(90)
    fd(6*k)
    left(90)
    fd(28*k)
up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()

from ipaddress import *
net = ip_network('191.128.66.83/255.192.0.0',  0)
print(net)

import math
def f(s,h):
    if s <= 35 and h == 3:
        return 1
    elif s > 35 and h ==3:
        return 0
    elif s <= 35 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(s - 1, h + 1) or f(s - 3, h + 1) or f(math.ceil(s / 2) , h + 1)
        else:
            return f(s - 1, h + 1) and f(s - 3, h + 1) and f(math.ceil(s / 2), h + 1)
for i in range(36,300):
    if f(i, 1):
        print(i)