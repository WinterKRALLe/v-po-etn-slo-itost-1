def insertionSort(arr, length):
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#############################################

def insertionSortRecursive(arr, length):
    if n <= 1:
        return
    insertionSortRecursive(arr, length - 1)
    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last
