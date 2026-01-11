f = open('9')
cnt = 0
for line in f.readlines():
    numbers = [int(x) for x in line.split()]
    numbers.sort()
    if numbers[3]**2 > (numbers[0] * numbers[1] * numbers[2]) or numbers[1] - numbers[0] == numbers[3] - numbers[2] and numbers[2] - numbers[1] == numbers[3] - numbers[2]:
        cnt += 1
print(cnt)