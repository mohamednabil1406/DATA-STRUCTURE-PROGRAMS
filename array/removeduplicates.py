def removeduplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1   # return length

arr = [1, 1, 2, 2, 3, 3]
k = removeduplicates(arr)

for i in range(k):
    print(arr[i], end=" ")
