def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_ptr = 1  # Position to write next unique element
    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[read_ptr - 1]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1
    return write_ptr

arr = [1, 1, 2, 2, 3]
length = remove_duplicates(arr)
print(arr[:length])  
