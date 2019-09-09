# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]: 
                smallest_index = j
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp





    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapping = 1
    while swapping == 1:
        swapping = 0
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                swapping = 1
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp



    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):


    #Find out maximum value
    for element in arr:
        if element < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if maximum < element:
            maximum = element
    
    #Create array of 0s to with maximum elements
    count = [0 for i in range(maximum + 1)]
    #tally up how many values are in each position in the array
    for x in arr:
        count[x] += 1


    result = []
    for i in range(len(count)):
        while count[i] > 0:
            result.append(i)
            count[i] -= 1


    


    return result