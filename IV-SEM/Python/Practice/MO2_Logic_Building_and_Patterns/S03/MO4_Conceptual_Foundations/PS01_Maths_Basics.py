'''
#basic arthemetic operations
a = 10
b = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b) # exponentiation
print(a // b)
#important built-in functions
print(abs(-5))  # absolute value
print(round(3.14159, 2))  # round to 2 decimal places
print(max(1, 5, 3))  # maximum value
print(min(1, 5, 3))  # minimum value
print(pow(2, 3))  # power function
print(sum([1, 2, 3, 4, 5]))  # sum of a list
'''
#find gcd using math and eclidean algorithm
import math
def gcd(a, b):
    return math.gcd(a, b)
def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a            
print(gcd(48, 18)) 
print(gcd_euclidean(48, 18))  

