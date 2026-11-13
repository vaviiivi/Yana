values = [3, -8, 19, -12, 6, 9]
for index in range(0, len(values)):
    if values[index] < 0:
        values[index] = 0
print(values)