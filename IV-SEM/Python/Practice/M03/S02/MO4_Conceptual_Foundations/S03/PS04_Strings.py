s='python'
s1='python'
s2='''python
is 
interesting
'''
'''
print(s+s1) #concatenation
print(s1*2) #repetition
print("on" in s) #membership operator
#string is a collection of characters, it is immutable it is enclosed in quotes
'''
s='python'
print(len(s)) #length of string
print(max(s)) #maximum character
print(min(s)) #minimum character
print(max("abc12234AASD")) #maximum character   
print(dir(str))
s = s.replace("y", "Y") #replace method
print(s)
print(s.find("on"))
print(s.find("xyz"))
s = input()
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
print(rev)
a = input()
b = input()
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not an Anagram")