# сортировка вставками

def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return arr


lst = list(map(int, input().split()))
print("Given array is: " + ', '.join(list(map(str, lst))))
print("Sorted array is: " + ', '.join(list(map(str, insertion_sort(lst)))))
