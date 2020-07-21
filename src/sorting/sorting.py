# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
        else:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
    return merged_arr + arrA + arrB


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    arrA = arr[middle:]
    arrB = arr[:middle]
    return merge(merge_sort(arrA), merge_sort(arrB))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, length, r):
    # Your code here
    pass
