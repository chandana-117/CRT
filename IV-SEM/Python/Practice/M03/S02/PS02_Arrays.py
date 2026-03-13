'''4 6  = list(map(int,input().split()))
n.sort()
print(n[::-1])
a = list(map(int,input().split()))
a.sort()
a.reverse()
print(a)
arr = list(map(int,input().split()))
rev = []
for i in arr:
    rev = [i] + rev
    rev.sort()
print(rev)
n=list(map(int,input().split()))
n.sort()
print(max(n))
print(min(n))

n=list(map(int,input().split()))
n.sort()
print("Second largest number is",n[-2])'''
n=list(map(int,input().split()))
n.sort()
print(list(set(n)))
