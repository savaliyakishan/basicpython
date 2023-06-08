# Count the total number of digits in a number
n = 456

rever = ""
while n > 0:
    digit = n % 10
    n = n // 10
    print(digit,end="")