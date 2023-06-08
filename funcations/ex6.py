# Create a recursive function

def func1(num):
    if num :
        return num + func1(num - 1)
    else:
        return 0

print(func1(10))
    