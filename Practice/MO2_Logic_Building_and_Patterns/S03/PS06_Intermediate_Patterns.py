'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
li=[1,2,3,4,5]
res=[]
for i in li:
    res.append(i*2)
print(res)
li=[1,2,3,4,5]
print([i*2 for i in li])
li=[1,2,3,4,5]
res=[]
for i in li:
    if i%2==0:
        res.append(i)
print(res)
li = [1, 2, 3, 4, 5]
print([i for i in li if i % 2 == 0])
print([i for i in li if i % 2 != 0])
print({i:i*2 for i in li if i % 2 == 0})

li1 =['a','b','c']
print(" ".join(li1))
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()'''

