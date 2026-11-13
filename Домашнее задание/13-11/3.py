values=[3,-8,19,-12,6,9]
new=[]
for i in range (len(values)):
    if i%3==0:
        new=new+[values[i]]

print(new)