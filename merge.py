def merge(arr1: list[int], arr2: list[int]):
    answer_arr = list()

    cursor1 = 0
    cursor2 = 0

    while cursor1 < len(arr1) and cursor2 < len(arr2):
        if arr1[cursor1] > arr2[cursor2]:
            answer_arr.append(arr2[cursor2])
            cursor2 += 1
        elif arr1[cursor1] == arr2[cursor2]:
            answer_arr.append(arr1[cursor1])
            answer_arr.append(arr2[cursor2])
            cursor1 += 1
            cursor2 += 1
        else:
            answer_arr.append(arr1[cursor1])
            cursor1 += 1

    if cursor1 == len(arr1):
        answer_arr += arr2[cursor2:]
    else:
        answer_arr += arr1[cursor1:]

    return answer_arr
