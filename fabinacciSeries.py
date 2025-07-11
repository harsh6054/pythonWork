#To display fabinacci series of given numbers
num=int(input("Enter Number:"))
n1=0
n2=1
n3=0
count=0
print("Fabinacci Series")
while count < num:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1
