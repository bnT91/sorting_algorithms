# функция выполняет сортировку слиянием.

import merge
import sys

sys.setrecursionlimit(2000)


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge.merge(arr1=left, arr2=right)


lst = list(map(int, input().split()))
print("Given array is: " + ', '.join(list(map(str, lst))))
print("Sorted array is: " + ', '.join(list(map(str, merge_sort(lst)))))
