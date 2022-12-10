def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

##################################

def bubbleSortRecursive(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            # Swap the two elements
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count += 1

    if count != 0:
        return bubbleSortRecursive(arr)

    return arr
