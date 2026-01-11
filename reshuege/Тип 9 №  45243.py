f = open('9')
cnt = 0
for line in f.readlines():
    numbers = [int(x) for x in line.split()]
    numbers.sort()
    if (numbers[0] + numbers[4])**2 > (numbers[1]**2 + numbers[2]**2 + numbers[3]**2):
        cnt += 1
print(cnt)