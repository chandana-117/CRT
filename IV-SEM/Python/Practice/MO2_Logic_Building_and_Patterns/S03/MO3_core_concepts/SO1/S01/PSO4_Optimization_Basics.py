'''a=[10,20,30,40,50]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i]+a[j])    #o(n^2)
a=[10,20,30,40,50]
for num in a:
    print(num+num)   #o(n)

a=[10,20,30,40,50]
sum1=0
for i in range(len(a)):
    sum1+=a[i]
print(sum1)          #o(n)

a=[10,20,30,40,50]
print(sum(a))         #o(n)

a=[]
for i in range(10):
    a.append(i*i)
print(a)              #o(n)

a=print([i*i for i in range(10)])   #o(n)
'''
#2) find the maximum element in the list
num = [10, 23, 54, 85, 10, 25]
max_num = num[0]
for i in range(1, len(num)):
    if num[i] > max_num:
        max_num = num[i]
print(max_num)        #o(n)



