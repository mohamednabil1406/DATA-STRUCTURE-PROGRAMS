def binarysearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return arr
arr = [1, 2, 4, 7, 9]
target = 7
result = binarysearch(arr, target)
print("Index:", result)  # Output: Index: 3