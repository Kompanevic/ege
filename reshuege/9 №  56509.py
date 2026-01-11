f = open('9')
cnt = 0
for line in f.readlines():
    numbers = [int(x) for x in line.split()]
    listp = [x for x in numbers if numbers.count(x) > 1]
    listn = [x for x in numbers if numbers.count(x) == 1]
    if len(listp) > 0 and len(listn) > 0:
        if ((sum(listp)) / len(listp)) < ((sum(listn) / len(listn))):
            cnt += 1
print(cnt)
