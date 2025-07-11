#To check Given Number is Prime or Not
num=int(input("Enter Number"))
flag =0
for i in range(2,num):
    if(num%2)==0:
        flag=1
        break
if(flag==1):
    print("Give Number is Not Prime")
else:
    print("Give Number isPrime")