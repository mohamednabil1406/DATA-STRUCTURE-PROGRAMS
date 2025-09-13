def linearsearcf(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[4,2,7,1,9]
target=7
result=linearsearcf(arr,target)
print("Index",result)