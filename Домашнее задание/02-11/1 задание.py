#  В диапазоне от 1 до 1000 вывести все простые числа.
b = []
for x in range(1,1001):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        b.append(x)
print(b)
