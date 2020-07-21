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
            return binary_search(arr, target, start, pivot)
        elif arr[pivot] < target:
            return binary_search(arr, target, pivot, end)
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

