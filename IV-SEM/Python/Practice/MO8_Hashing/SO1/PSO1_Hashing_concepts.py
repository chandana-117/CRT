'''#set empty
s=set()
print(type(s))

#dictionary
d={}
d[1]='a'
d.update({2:'b', 3:'c'})
d.setdefault(4,'d')
#fetch the value
d.get(3)
d.get(100,0) #if key is not present return 0
#frequency of each element in the array
def frequency(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
arr=[1,2,3,4,5,1,2,3,4,5,1,2,3]
print(frequency(arr))

#return the frequency of each element in the array using get
def frequency(arr):
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    return d
arr=[1,2,3,4,5,1,2,3,4,5,1,2,3]
print(frequency(arr))

#return the element with maximum frequency in the array
def max_frequency(arr):
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    max_freq=0
    max_freq_element=None
    for key,value in d.items():
        if value>max_freq:
            max_freq=value
            max_freq_element=key
    return max_freq_element
arr=[1,2,3,4,5,1,2,3,4,5,1,2,3]
print(max_frequency(arr))
'''
#return the element with maximum frequency in the array using counter
from collections import Counter
def max_frequency(arr):
    c=Counter(arr)
    return c.most_common(1)[0][0]
arr=[1,2,3,4,5,1,2,3,4,5,1,2,3]
print(max_frequency(arr))