def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

def armstrong_in_interval(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print("Armstrong numbers between", start, "and", end, "are:", armstrong_in_interval(start, end))
