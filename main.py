import matplotlib.pyplot as plt
from insertsort import insertionSort, insertionSortRecursive
from bubblesort import bubbleSort, bubbleSortRecursive
from quicksort import quickSort, quickSortRecursive
import numpy as np
import time, sys

sys.setrecursionlimit(20000)


def plotShow():

    sorts = [
        # {
        #     "name": "Bubble Sort",
        #     "sort": lambda arr: bubbleSort(arr, len(arr))
        # },
        # {
        #     "name": "Insertion Sort",
        #     "sort": lambda arr: insertionSort(arr)
        # },
        {
            "name": "Quick Sort",
            "sort": lambda arr: quickSort(arr, 0, len(arr) - 1)
        },
        # {
        #     "name": "Bubble Sort Recursive",
        #     "sort": lambda arr: bubbleSortRecursive(arr)
        # },
        # {
        #     "name": "Insertion Sort Recursive",
        #     "sort": lambda arr: insertionSortRecursive(arr)
        # },
        {
            "name": "Quick Sort Recursive",
            "sort": lambda arr: quickSortRecursive(arr, 0, len(arr) - 1)
        }
    ]

    elements = np.array([i*1000 for i in range(1, 10)])

    plt.xlabel('Array Length')
    plt.ylabel('Time Complexity')

    for sort in sorts:
        times = list()
        start_all = time.time()
        for i in range(1, 10):
            start = time.time()
            a = np.random.randint(1000, size = i * 1000)
            sort["sort"](a)
            end = time.time()
            times.append(end - start)

            print(sort["name"], "Sorted", i * 1000, "Elements in", end - start, "s")
        end_all = time.time()
        print(sort["name"], "Sorted Elements in", end_all - start_all, "s")

        plt.plot(elements, times, label = sort["name"])

    plt.grid()
    plt.legend()
    plt.show()


plotShow()