# функция quick_sort должна выполнять быструю сортировку массива:
# входные данные: изначальный массив
# выходные данные: массив с числами в порядке возрастания

import sys

sys.setrecursionlimit(2000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    main_elem = arr[0]
    left = list(filter(lambda x: x < main_elem, arr))  # числа, меньшие опорного элемента
    middle = [i for i in arr if i == main_elem]  # числа, равные опорному элементу
    right = list(filter(lambda x: x > main_elem, arr))  # числа, большие опорного элемента

    return quick_sort(left) + middle + quick_sort(right)


lst = list(map(int, input().split()))
print("Given array is: " + ', '.join(list(map(str, lst))))
print("Sorted array is: " + ', '.join(list(map(str, quick_sort(lst)))))
