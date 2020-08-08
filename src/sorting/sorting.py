# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here

    # vars for index
    a_index, b_index = 0, 0

    # vars for len
    lenA, lenB = len( arrA ), len( arrB )

    # nested functions for DRY
    def mrgA():
        nonlocal a_index
        merged_arr.append( arrA[ a_index ] )
        a_index += 1

    def mrgB():
        nonlocal b_index
        merged_arr.append( arrB[ b_index ] )
        b_index += 1

    # while both A and B
    while a_index < lenA and b_index < lenB:
        if arrA[ a_index ] < arrB [ b_index ]:
            mrgA()
        else:
            mrgB()
    
    # append the rest of A
    while a_index < lenA:
        mrgA()

    # append the rest of B
    while b_index < lenB:
        mrgB()

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    mid = len( arr ) // 2
    if len( arr ) > 1:
        side_a = merge_sort( arr[ :mid ] )
        side_b = merge_sort( arr[ mid: ] )
        arr = merge( side_a, side_b )

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
