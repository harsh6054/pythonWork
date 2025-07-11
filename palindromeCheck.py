#To check Given string palindrome or not
s1=input("Enter String:")
s2=""
for i in s1:
    s2=i+s2
if(s1==s2):
    print("Given String Are Palindrome")
else:
    print("Given String Are not Palindrome")
