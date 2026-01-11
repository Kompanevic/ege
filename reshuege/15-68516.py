for a in range(1,300):
    Flag = True
    for x in range(0,300):
        if ((x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == 0:
            Flag = False
            break
    if Flag:
        print(a)