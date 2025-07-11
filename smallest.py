#Find smallest of 3 Numbers
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
if(a<b):
    if(a<c):
        print("A is Smallest")
    elif(b<c):
        print("B is Smallest")
else:
    print("C is Smallest")
