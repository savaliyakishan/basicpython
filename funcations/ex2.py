#  Create a function with variable length of arguments

def func1(*num):
    for i in num:
        print(i)
func1(15,25,35,56)