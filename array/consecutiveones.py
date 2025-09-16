def findones(nums):
    c=0
    m=0
    for i in range(len(nums)):
        if nums[i]==1:
            c+=1
        else:
            c=0
    m=max(m,c)
    return m
nums=[1,1,0,1,1,1]
print("The consecutive ones",findones(nums))


"or"

def findzeros(arr):
    c=0
    m=0
    for i in range(len(arr)):
        if arr[i]==0:
            c+=1
        else:
            c=0
    m=max(m,c)
    return m
arr=[0,0,1,0,0,0]
print("the consecuitves zeros",findzeros(arr))