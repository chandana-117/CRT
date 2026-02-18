'''
n=int(input())
for i in range(n):
    for j in range(n):
        print("*" , end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()

n=int(input())
num=1   
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end =" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

