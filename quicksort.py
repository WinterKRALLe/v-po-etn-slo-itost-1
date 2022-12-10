def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]

    for j in range(l , h):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortRecursive(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        if pivot > 1:
            quickSortRecursive(arr, left, pivot - 1)

        if pivot + 1 < right:
            quickSortRecursive(arr, pivot + 1, right)

###########################################

def quickSort(arr, l, h):
    if l >= h:
        return arr

    size = h - l + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

    return arr