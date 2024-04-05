def binary_search(arr, target):
    #Here implement a way to sort the array

    sorted_array = arr.sorted()
    left, right = 1, len(arr)-1
    while left < right:
        middle = int(round((left+right)/2, 0))
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        if arr[middle] > target:
            right = middle - 1
    return False