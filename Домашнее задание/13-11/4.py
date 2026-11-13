values=[3,-8,19,-12,6,9]
x=0
for i in range (len(values)):
    if values[i]<0:
        x=i
if x!=0:
    values[x]=0
print(values)