def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#############################################

def insertionSortRecursive(arr):
    if len(arr) == 1:
        return arr

    key = arr[0]

    sorted_array = insertionSortRecursive(arr[1:])

    for i in range(len(sorted_array)):
        if key < sorted_array[i]:
            return sorted_array[:i] + [key] + sorted_array[i:]

    return sorted_array + [key]
