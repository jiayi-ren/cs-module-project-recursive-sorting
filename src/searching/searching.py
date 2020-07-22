# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1
    if start <= end:
        pivot = start + (end - start) //2
        if arr[pivot] == target:
            return pivot
        elif arr[pivot] > target:
            return binary_search(arr, target, start, pivot-1)
        elif arr[pivot] < target:
            return binary_search(arr, target, pivot+1, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1
    
    left = 0
    right = len(arr) -1
    is_ascending = arr[left] < arr[right]
    while left <= right:
        pivot = left+ (right - left)//2
        if arr[pivot] == target:
            return pivot
        if is_ascending:
            if arr[pivot] > target:
                right = pivot -1
            elif arr[pivot] < target:
                left = pivot +1
        else:
            if arr[pivot] > target:
                left = pivot+1
            elif arr[pivot] < target:
                right = pivot-1

    return -1  # not found