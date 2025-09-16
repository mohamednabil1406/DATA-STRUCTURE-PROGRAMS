def missing_number(arr,n):
    actual=n*(n+1)//2
    total=sum(arr)
    missing=actual-total
    return missing
arr=[1,2,4]
n=4
print(missing_number(arr,n))
