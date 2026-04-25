def sum_of_list(lst):
    total = 0
    stop = -1*(len(lst)+1)
    for i in range(-1, stop, -1):
        total += lst[i]
    return total
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
print(sum_of_list([10, 20, 30]))       # Output: 60

def array_sum1(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + array_sum1(nums[1:])
print(array_sum1([10,20,30,40]))  # Output: 100
#using recursive calls
def array_sum2(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[-1] + array_sum2(nums[:-1])
print(array_sum2([10,20,30,40]))  # Output: 100
#reverse a list
def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
def reverse_list_swap(lst, start, end):
    if start >= end:
        return lst
    lst[start], lst[end] = lst[end], lst[start]
    return reverse_list_swap(lst, start + 1, end - 1)
print(reverse_list_swap([1, 2, 3, 4, 5], 0, 4))  # Output: [5, 4, 3, 2, 1]
#reverse a string using recursive calls
def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("Hello"))  # Output: "olleH"
#reverse a function using palindorme function
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
 