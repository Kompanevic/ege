f = open('9')
kol = 0
for line in f.readlines():
    numbers = [int(x) for x in line.split()]
    numbers.sort()
    cnt = 0
    if numbers[0] > numbers[1] and numbers.count(numbers[0]) == 1:
        cnt += 1
    if numbers[5] > numbers[4] and numbers.count(numbers[5]) == 1:
        cnt += 1
    for i in range(1,len(numbers) - 1):
        Flag = False
        if numbers.count(numbers[i]) > 1:
            Flag = True
        if numbers.count(numbers[i]) == 1 and numbers[i] < numbers[i + 1] and numbers[i] < numbers[i - 1]:
            cnt += 1
    if cnt == 3:
        kol += 1
        print(kol)


