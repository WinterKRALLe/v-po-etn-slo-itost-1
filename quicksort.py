def Partition(arr, left, right):
    temp = 0
    pivot = arr[left]
    while True:
        while arr[left] < pivot:
            left+=1

        while arr[right] > pivot:
            right-=1

        if left < right:
            temp = arr[right]
            arr[right] = arr[left]
            arr[left] = temp
        else:
            return right


def quickSortRecursive(arr, left, right):
    pivot = 0
    if left < right:
        pivot = Partition(arr, left, right)
        if pivot > 1:
            quickSortRecursive(arr, left, pivot - 1)

        if pivot + 1 < right:
            quickSortRecursive(arr, pivot + 1, right)

###########################################

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]

    for j in range(l , h):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSort(arr,l,h):
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition( arr, l, h )

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
