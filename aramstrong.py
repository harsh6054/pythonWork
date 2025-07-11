#To check Aramstrong number or not
num = int(input("Enter Number:"))
sum = 0
temp = num
while temp > 0:
    n1 = temp % 10
    sum += n1 ** 3
    temp //= 10
if num == sum:
    print("Given Number is Armstrong number")
else:
    print("Given Number is Not Armstrong number")