def major(arr):
    n = len(arr)
    for i in range(n):
        c = 0
        for j in range(n):
            if arr[j] == arr[i]:
                c += 1
        if c > n // 2:
            return arr[i]
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
print("Majority element:", major(arr))  # prints the result

print("Array elements:", end=" ")
for num in arr:
    print(num, end=" ")
