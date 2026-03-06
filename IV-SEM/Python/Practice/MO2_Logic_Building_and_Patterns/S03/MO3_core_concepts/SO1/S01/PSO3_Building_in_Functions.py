'''arr=[10,23,54,85,10,25]
print(max(arr))

word='madam'
if word=="".join(reversed(word)):
    print("Palindrome")
else:
    print("Not a Palindrome")

nums = list(map(int, input().split()))
even = list(filter(lambda x: x % 2 == 0, nums))
print(len(even))

nums = [10, 23, 54, 85, 10, 25]
unique = list(set(nums))
print(unique)
number = 12345
result = sum(int(digit) for digit in str(number))
print(result)

words = ["banana", "apple", "mango", "orange"]
sorted_words = sorted(words)
print(sorted_words)
list1 = [1, 2, 3,4,5,]
list2 = [4, 5, 6]
common = list(set(list1) & set(list2))
print(common)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for index,value in enumerate(fruits):
    print(index,value)
list1 = ["apple", "banana", "cherry", "date", "elderberry"]
list2 = [1, 2, 3, 4, 5]
for a, b in zip(list1, list2):
    print(a, b)
'''
num = [10, 23, 54, 85, 10, 25]
arr = sorted(num)
print(arr[4])

