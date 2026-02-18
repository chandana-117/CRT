'''n=int(input())
for i in range(1,n+1):   #print numbers from 1 to n
    print(i)

for i in range(2,n+1,2): 
      print(i)  
    #print even numbers from 2 to n
for i in range(1,n+1,2): 
      print(i)
    #print odd numbers from 1 to n
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a,b=b,c
    #print first n Fibonacci numbers

n=int(input())
for i in range(1,21):
     print(n,"x",i,"=",n*i) #print multiplication table of n

n=int(input())
for i in range(1,n+1):
     print(i**2) #print squares of numbers from 1 to n
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(-i,end=" ") #print even numbers as negative from 1 to n
    else:
        print(i,end=" ")  #print odd numbers as positive from 1 to n
'''
n=int(input())
num=1
add=1
for i in range(n):
    print(num,end=" ")  #print first n odd numbers
    num+=add
    add += 1