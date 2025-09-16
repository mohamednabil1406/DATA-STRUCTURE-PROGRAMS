def getsingle(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        c = 0
        for j in range(n):
            if arr[j] == num:
                c += 1
        if c == 1:   # check inside the loop
            return num
    return -1

arr = [4, 1, 2, 1, 2]
print(getsingle(arr))


"xor method"

def get(arr):
    xor=0
    for num in arr:
        xor^=num
    return xor
arr=[4,1,2,1,2]
print("the xor",get(arr))
