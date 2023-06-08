#  Calculate the multiplication and sum of two numbers

num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))
mul = num1 * num2
if mul > 1000:
    sumnum = num1 + num2
    print(f"The result is {sumnum}")
else:
    print(f"The result is {mul}")