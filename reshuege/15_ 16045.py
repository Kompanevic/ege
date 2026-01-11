for a in range(0,300,1):
    Flag = True
    for x in range(0,300):
        for y in range(0,300):
             if ((y + 2*x != 48) or (a < x) or (a < y)) == 0:
                Flag = False
                break
    if Flag:
        print(a)