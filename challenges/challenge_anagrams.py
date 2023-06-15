def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return ''.join(result)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    sorted_string1 = merge_sort(first_string)
    sorted_string2 = merge_sort(second_string)
    if first_string == '' and second_string == '':
        return '', '', False
    if sorted_string1 == sorted_string2:
        return sorted_string1, sorted_string2, True
    else:
        return sorted_string1, sorted_string2, False
