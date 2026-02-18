'''
write a python code to check whether numbwe is prime or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


arr=list(map(int,input("Enter array element:").split()))
inc=True
dec=True
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        dec=False
    elif arr[i]>arr[i+1]:
        inc=False
if inc:
    print("Array is increasing")
elif dec:
    print("Array is decreasing")
else:
    print("Array is neither increasing nor decreasing")
'''

roman=input("Enter a Roman numeral: ").upper()
values ={
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
total = 0
for ch in range(len(roman)):
    if ch < len(roman) - 1 and values[roman[ch]] < values[roman[ch+1]]:
        total -= values[roman[ch]]
    else:
        total += values[ch]
    
        