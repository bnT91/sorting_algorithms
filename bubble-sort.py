# сортировка пузырьком

import sys

sys.setrecursionlimit(2000)


def bubble_sort(arr):
    new_arr = arr.copy()
    for i in range(len(new_arr)):
        for j in range(len(new_arr) - i - 1):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j+1], new_arr[j] = new_arr[j], new_arr[j+1]

    return new_arr


lst = list(map(int, input().split()))
print("Given array is: " + ', '.join(list(map(str, lst))))
print("Sorted array is: " + ', '.join(list(map(str, bubble_sort(lst)))))
