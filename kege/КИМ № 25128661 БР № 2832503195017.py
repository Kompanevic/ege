import math
def f(s,h):
    if s <= 30 and h == 3:
        return 1
    elif s <= 30 and h < 3:
        return 0
    elif s > 30 and h == 3:
        return 0
    else:
        if h % 2 == 0:
            return f(s - 3,h + 1) or f(s - 6, h + 1) or f(math.ceil(s *  0.4), h + 1)
        else:
            return f(s - 3, h + 1) and f(s - 6, h + 1) and f(math.ceil(s * 0.4), h + 1)
for i in range(31,300):
    if f(i,1):
       print(i)

import math
def f(s,h):
    if s <= 30 and h == 4:
        return 1
    elif s <= 30 and h < 4:
        return 0
    elif s > 30 and h == 4:
        return 0
    else:
        if h % 2 == 1:
            return f(s - 3,h + 1) or f(s - 6, h + 1) or f(math.ceil(s *  0.4), h + 1)
        else:
            return f(s - 3, h + 1) and f(s - 6, h + 1) and f(math.ceil(s * 0.4), h + 1)
for i in range(31,300):
    if f(i,1):
       print(i)

import math
def f(s,h):
    if s <= 30 and (h == 3 or h == 5):
        return 1
    elif s <= 30 and h < 5:
        return 0
    elif s > 30 and h == 5:
        return 0
    else:
        if h % 2 == 0:
            return f(s - 3,h + 1) or f(s - 6, h + 1) or f(math.ceil(s *  0.4), h + 1)
        else:
            return f(s - 3, h + 1) and f(s - 6, h + 1) and f(math.ceil(s * 0.4), h + 1)
for i in range(31,300):
    if f(i,1):
       print(i)

for a in range(30000):
    Flag = False
    for x in range(0,66666):
        if (((7*x + 12) < 456789) and (a < (3*x + 5180))) == 0:
            Flag =  True
            break
    if Flag:
        print(a)

from ipaddress import *
net = ip_network('172.30.160.0/255.255.240.0',0)
kol = 0
for ip in net:
    s = bin(ip.packed[0])[2:]
    f = bin(ip.packed[1])[2:]
    r = bin(ip.packed[2])[2:]
    x = bin(ip.packed[3])[2:]
    if (s.count('1') == x.count('1')) and (f.count('0') != r.count('0')):
        kol += 1a

