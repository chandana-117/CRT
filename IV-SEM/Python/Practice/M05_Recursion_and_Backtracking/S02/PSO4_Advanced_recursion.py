def Digital_Root(n):
    if n < 10:
        return n
    else:
        sum_digits = sum(int(digit) for digit in str(n))
        return Digital_Root(sum_digits)
print(Digital_Root(16))  # Output: 7
print(Digital_Root(942)) # Output: 6
#check if array is sorted using recursion
def is_sorted(arr, index=0):
    if index == len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)
print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([1, 3, 2, 4, 5]))  # Output: False

#sorted check using recursion
def is_sorted(nums):
    if len(nums) <= 1:
        return True
    if nums[0] > nums[1]:
        return False
    return is_sorted(nums[1:])
print(is_sorted([1,2,3,4,5]))  #Output:True
print(is_sorted([1,3,2,4,5]))  #Output:False
