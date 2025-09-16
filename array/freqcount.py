def frequency(arr, n):
    freq = {}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    for x in freq:
        print(x, freq[x])

arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
frequency(arr, n)
