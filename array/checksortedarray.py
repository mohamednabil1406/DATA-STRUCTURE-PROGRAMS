def issorted(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:

               return False
        return True
arr=[5,2,3,4,5]
n=len(arr)
ans=issorted(arr,n)
if ans:
    print("True")
else:
    print("False")



    #or

def is_sorted(arr, n):
    for i in range(1, n):   # start from index 1
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [1, 2, 3, 4]
n = len(arr)
ans = is_sorted(arr, n)

if ans:
    print("Correct")
else:
    print("Not Correct")
