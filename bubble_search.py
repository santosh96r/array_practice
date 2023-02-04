def bubble_search(elements):
    size = len(elements)

    for i in range(size-1):
        for j in range(size-1 ):
            if elements[j] > elements[j+1]:

                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp

    return elements

elements = [88, 45, 7, 66, 99, 3, 19, 32, 24, 66, 43, 105, 73]
print(bubble_search(elements))