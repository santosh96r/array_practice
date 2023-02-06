def reverse_array(number_list, start , end ):
    # arr1 = []
    start = 0
    end = len(number_list) -1
    while start < end :
        number_list[start], number_list[end] =number_list[end], number_list[start]
        start = start +1
        end = end -1

    return number_list

number_list = [1, 2, 3, 5, 6, 8, 7, 9, 10]
print(reverse_array(number_list, 0, 8))
