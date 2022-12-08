def bubbleSort(arr, length):
  for i in range(length):
    for j in range(0, length - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

##################################

def bubbleSortRecursive(arr, length):
    count = 0
    for idx in range(length-1):
        if arr[idx] > arr[idx + 1]:
            arr[idx],arr[idx + 1] = arr[idx + 1],arr[idx]
            count += 1
    if count == 0:
        return arr
    else:
        return bubbleSortRecursive(arr)
