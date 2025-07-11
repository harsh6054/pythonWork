#find Gretest of given 3 Numbers
a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))
c=int(input("Enter Number C:"))
if(a>b):
    if(a>c):
        print("A is Greater")
    elif(b>c):
        print("B is Greater")
else:
    print("C is Greater")
