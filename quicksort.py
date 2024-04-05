def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)
        
def partition(arr, left, right):
    #Pivot here will always be the last element of the array.
    pivot = arr[right]
    
    i = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

'''
Quicksort is a way to sort a array 
'''