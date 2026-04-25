'''
Linear search (sequential search)
Binary search (interval search)

def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(LinearSearch([12,23,63,5,78,10],63))  #Output:2
print(LinearSearch([12,23,63,5,78,10],100))  #Output:-1
'''
#Binary search using sort
def BinarySearch(arr, target):
    arr.sort()  
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr=list(map(int,input().split()))
target=int(input())
print(BinarySearch(arr, target))
 