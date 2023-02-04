def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        elif mid_number < number_to_find:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return -1

number_list = [5, 13, 19, 24, 36, 44, 52, 59, 67, 74, 83, 99]
number_to_find = 24

print(binary_search(number_list, number_to_find))