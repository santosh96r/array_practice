# def show_arguments(arg1, *args ):
#     print("1st argument is {}".format(arg1))
#
#     for i in args :
#         print("remainng arguments are {}".format(i))
#
# show_arguments('skr', 123, 'mk', [12, 34])

# def show_karg(args1, **args):
#     print('1st arg is {}'.format(args1))
#
#     for key, word in args.items():
#         print(key, word)
#
#
# show_karg('skr', age  = 25,city= 'bbsr')

# str1 = " do your work yourself"
# l = list(str1)
# print(l)
# l = str1.split()
# d = {}
# for i in l :
#     d[i] = len(i)
# print(d)
# l2 = []
# for key, value in d.items():
#     l2.append(value)
#
#     # print(value)
# print(l2)
# maxm = max(l2)
# print(maxm)

# def binary_search(numbers_list, number_to_find):
#     left_index = 0
#     right_index = len(numbers_list)
#     mid_index = 0
#     while left_index <= right_index:
#         mid_index = (left_index+right_index) //2
#         mid_number = numbers_list[mid_index]
#
#         if mid_number == number_to_find:
#             return mid_index
#         elif mid_number < number_to_find:
#             left_index = mid_index -1
#
#         else :
#             right_index = mid_index +1
#
#     return -1
#
# numbers = [25, 14, 22, 36, 37, 66, 45, 55, 98, 89, 78, 72, 101, 555, 8]
# num_to_find = 45
# print(binary_search(numbers, num_to_find))

# def binary_search(number_list, target):
#     left_index = 0
#     right_index = len(number_list)-1
#     mid_index = 0
#     while left_index <= right_index:
#         mid_index = (left_index + right_index) //2
#         mid_number = number_list[mid_index]
#         if mid_number == target:
#             return mid_index
#         elif mid_number < target:
#             left_index = mid_index + 1
#         else :
#             right_index = mid_index - 1
#     return -1
#
#
# numbers = [5, 13, 19, 24, 36, 44, 52, 59, 67, 74, 83, 99]
# target = 99
# print(binary_search(numbers, target))

# def bubble_sort(elements):
#     size = len(elements)
#     for i in range(size-1):
#         for j in range(size-1):
#             if elements[j] > elements[j+1]:
#                 temp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1 ] = temp
#
#     return elements
#
# elements = [88, 45, 7, 66, 99, 3, 19, 32, 24, 66, 43, 105, 73]
# print(bubble_sort(elements))

