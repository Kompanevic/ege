f = open('9')
cnt = 0
for line in f.readlines():
    numbers = [int(x) for x in line.split()]
    numbers.sort()
    listp = [x for x in numbers if numbers.count(x) > 1]
    listn = [x for x in numbers if numbers.count(x) == 1]
    if len(listn) == 0 :
        continue
    sqmin = min(listn)**2
    sqmax = max(listn)**2
    snpov = sum(listn) - min(listn) - max(listn)
    if (numbers.count(numbers[0]) == 2  and len(listn) == 6 or numbers.count(numbers[0]) == 3 and len(listn) == 5) and sqmax + sqmin <= (snpov**2):
        cnt += 1
print(cnt)
