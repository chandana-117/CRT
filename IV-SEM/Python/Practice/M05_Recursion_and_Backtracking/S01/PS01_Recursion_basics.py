def Natural_sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
print(Natural_sum(5))  # Output: 15
print(Natural_sum(10)) # Output: 55
def Factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1) 
print(Factorial(5))  # Output: 120
print(Factorial(0))  # Output: 1
print(Factorial(9))  # Output: 362880
def Fibonacci(n):
    if n <= 0:
        return "Fibonacci is not defined for negative numbers"
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(5))  # Output: 3
print(Fibonacci(7)) # Output: 8