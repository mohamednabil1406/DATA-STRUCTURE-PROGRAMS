def largestelement(arr):
    arr.sort()
    return arr[-1]
arr=[5,4,7,8,6]
print(largestelement(arr))


#recursive approach 

def largestmax(arr,n):
    max=arr[0]
    for i in range(0,n):
        if arr[i]==max:
            max=arr[i]
    return max
arr=[8,4,3,2,1]
n=5
print(f"the laregst element in the {arr}:",largestmax(arr,n))