def two_sum(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        new=arr[l]+arr[r]
        if new==target:
            return (l,r)
        elif new<target:
            l+=1
        else:
            r-=1
    return -1
arr = [1, 2, 4, 7, 11, 15]
target = 15
print(two_sum(arr, target)) 