def Linear_Search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return i
    return -1
print(Linear_Search([1, 2, 3, 4, 5], 3))  # Output: 2
print(Linear_Search([1, 2, 3, 4, 5], 6))  # Output: -1
print(Linear_Search([1, 2, 3, 4, 5], 1))  # Output: 0
