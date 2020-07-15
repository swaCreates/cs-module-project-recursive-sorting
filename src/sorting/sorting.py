# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    j = 0
    k = 0

    for i in range(elements): # go through elements (both arr's)
        if j == len(arrA): # if index in arrA is length 0
            merged_arr[i] = arrB[k] 
            k += 1
        elif k == len(arrB):
            merged_arr[i] = arrA[j]
            j += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    print(f'splitting list: {arr}')

    if len(arr) > 1: # as long as arr is greater than len of 1
        mid = len(arr) // 2 # find middle of arr
        lhs = arr[:mid] # splicing arr from beginning to middle
        rhs = arr[mid:] # splicing arr from middle to end

        merge_sort(lhs) # keep splitting arr until it is len of 1
        merge_sort(rhs) # keep splitting arr until it is len of 1
    
        i=j=k=0 # each var equals 0

        while i < len(lhs) and j < len(rhs): # while len of each side of arr is greater than 0 (looping through)
            if lhs[i] < rhs[j]: # if val of lhs is < val of rhs
                arr[k] = lhs[i] # enter lhs val into first index of arr
                i += 1 # increment to the next position on lhs
                k += 1 # increment to the next position in arr
            else: # if rhs val is < lhs val (repeat steps above )
                arr[k] = rhs[j] 
                j += 1
                k += 1

        while i < len(lhs): # while len of lhs > 0
            arr[k] = lhs[i] # enter lhs val into first index of arr
            i += 1 
            k += 1

        while j < len(rhs): # (same steps above)
            arr[k] = rhs[j]
            j += 1
            k += 1

        merge(lhs, rhs) # merging lists from helper function
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

