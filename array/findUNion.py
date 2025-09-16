def union(arr1,arr2):
    freq={}
    unionset=[]
    for num in arr1:
        freq[num]=freq.get(num,0)+1
    for num in arr2:
        freq[num]=freq.get(num,0)+1
    for num in freq:
        unionset.append(num)
    return unionset
arr1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2=arr2 = [2, 3, 4, 4, 5, 11, 12]
unionset=union(arr1,arr2)
print("the union of two array")
for num in unionset:
    print(num,end=" ")