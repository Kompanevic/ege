for a in range(0,32):
    Flag = True
    for x in range(0,32):
         if ((x&9!=0) or (x&19==0) or (x&a!=0)) == 0:
            Flag = False
            break
    if Flag:
        print(a)