# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    curr = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr[curr] = arrA.pop(0)
            curr += 1
        else:
            merged_arr[curr] = arrB.pop(0)
            curr += 1
    if len(arrA) > 0:
        for i in arrA:
            merged_arr[curr] = i
            curr += 1
    if len(arrB) > 0:
        for i in arrB:
            merged_arr[curr] = i
            curr += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left_array = arr[:mid]
    right_array = arr[mid:]
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    arr = merge(left_array, right_array)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

