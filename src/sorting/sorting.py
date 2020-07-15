# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    j = 0
    k = 0

    for i in range(elements): # go through elements (both arr's)
        if j == len(arrA): # if index in arrA is length 0 (if nothing in arrA)
            merged_arr[i] = arrB[k] # enter elements in arrB
            k += 1 # increment through arrB
        elif k == len(arrB): # if index in arrB is length 0 (if nothing in arrB)
            merged_arr[i] = arrA[j] # enter elements in arrA 
            j += 1 # increment through arrA
        elif arrA[j] < arrB[k]: # if val in arrA < val in arrB
            merged_arr[i] = arrA[j] # enter value in arrA first into mergedArr
            j += 1 # increment through arrA
        else: # (vice versa)
            merged_arr[i] = arrB[k]
            k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    print(f'splitting list: {arr}')

    if len(arr) <= 1: #base case
        return arr

    if len(arr) > 1: # as long as arr is greater than len of 1
        mid = len(arr) // 2 # find middle of arr
        lhs = arr[:mid] # splicing arr from beginning to middle
        rhs = arr[mid:] # splicing arr from middle to end

        lhs = merge_sort(lhs) # keep splitting arr until it is len of 1
        rhs = merge_sort(rhs) # keep splitting arr until it is len of 1

        arr_merge = merge(lhs, rhs)

        return arr_merge
    
        # i=j=k=0 # each var equals 0

        # while i < len(lhs) and j < len(rhs): # while len of each side of arr is greater than 0 (looping through)

        #     # Check if current element  
        #     # of first array is smaller  
        #     # than current element of  
        #     # second array. If yes,  
        #     # store first array element  
        #     # and increment first array 
        #     # index. Otherwise do same  
        #     # with second array 

        #     if lhs[i] < rhs[j]: # if val of lhs is < val of rhs
        #         arr[k] = lhs[i] # enter lhs val into first index of arr
        #         i += 1 # increment to the next position on lhs
        #         k += 1 # increment to the next position in arr
        #     else: # if rhs val is < lhs val (repeat steps above)
        #         arr[k] = rhs[j] 
        #         j += 1
        #         k += 1

        # # Store remaining elements 
        # # of first array         

        # while i < len(lhs): # while len of lhs > 0
        #     arr[k] = lhs[i] # enter lhs val into first index of arr
        #     i += 1 
        #     k += 1
        
        # # Store remaining elements  
        # # of second array 

        # while j < len(rhs): # (same steps above)
        #     arr[k] = rhs[j]
        #     j += 1
        #     k += 1

        # merge(lhs, rhs) # merging lists from helper function
    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

