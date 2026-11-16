def n(nums):
    x=[]
    y=[]
    for i in range(0,len(nums)):
        if nums[i] in x:
            y.append(nums[i])
        else:
            x.append(nums[i])
    nums=[*x,*y]
    return len(x)