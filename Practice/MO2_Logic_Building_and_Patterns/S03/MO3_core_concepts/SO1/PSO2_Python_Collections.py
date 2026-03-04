'''def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
print(running_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]
print(running_sum([3,1,2,10,1]))  # Output: [3, 4, 6, 16, 17]
print(running_sum([4,5,3,7,8,9]))  # Output: [4, 9, 12, 19, 27, 36]
def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
     if nums[i] == nums[i-1]:
        return True
    return False
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
print(contains_duplicate([1, 3 ,5,6]))  # Output: False
def maxwel (accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth
print(maxwel([[1, 2, 3], [3, 2, 1]]))  # Output: 6
print(maxwel([[1, 5], [7, 3], [3, 5]]))  # Output: 10
def concat_arrays(nums):
    return(2*nums)
print(concat_arrays([1, 2, 3]))  # Output: [1, 2, 3, 1, 2, 3]

t=(10,23,143,12,23,45)
t2 = ("sai","kalyani","priya")
print(t[0])
print(t[-1])
print(t + t2)
print(t,t2)
print(t*5)
print(t[1:4])
print(t[:5])
print(t[:-1])
#intersection of two arrays
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return tuple((set1) &  (set2))
print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]
'''
#robot return to origin
def judge_circle(moves):
    x = 0
    y = 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
    return x == 0 and y == 0        
print(judge_circle("UD"))  # Output: True
print(judge_circle("LL"))  # Output: False
