ans = list()
for a1 in range(24,117):
    for a2 in range(a1,117):
        Flag = True
        for x in range(-1000,1000):
            if ((25 <= x <= 64) <= (((40 <= x <= 115) and (not(a1 <= x <= a2))) <= (not(25 <= x <= 64)))) == 0:
                Flag = False
                break
        if Flag:
            ans.append(a2-a1)
print(min(ans))