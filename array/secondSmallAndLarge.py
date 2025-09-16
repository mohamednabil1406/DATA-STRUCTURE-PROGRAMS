def getelement(arr,n):
    if n==0 or n==1:
        print(-1,-1)
    arr.sort()
    small=arr[1]
    large=arr[n-2]
    print("the econd Small",small)
    print("the second largest",large)

arr=[2,5,3,21,6]
n=len(arr)
getelement(arr,n)