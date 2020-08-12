# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
    # sanity check
    if start > end:
        return -1

    # find middle
    mid = ( start + end ) // 2

    # is target the middle?
    if arr[ mid ] == target:
        return mid

    # is target between middle and end?
    if arr[ mid ]  < target:
        return binary_search( arr, target, mid, end )

    # is target between start and middle?
    if arr[ mid ]  > target:
        return binary_search( arr, target, start, mid ) 

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
