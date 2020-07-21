# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    middle = start + end // 2
    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target, start=None, end=None, asc=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    middle = (start + end) // 2
    if asc is None:
        asc = arr[start] < arr[end]
    if asc:
        if arr[start] > arr[end]:
            return -1
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            return agnostic_binary_search(arr, target, start, middle - 1, asc)
        else:
            return agnostic_binary_search(arr, target, middle + 1, end, asc)
    else:
        if arr[end] > arr[start]:
            return -1
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            return agnostic_binary_search(arr, target, middle + 1, end, asc)
        else:
            return agnostic_binary_search(arr, target, start, middle - 1, asc)
