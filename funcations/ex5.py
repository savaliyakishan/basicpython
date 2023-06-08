# Create an inner function to calculate the add in the following way


# outer function
def fun1(a, b):
    square = a ** 2
    def addfun(a, b):
        return a + b
    add = addfun(a, b)
    return add + 5
result = fun1(5, 10)
print(result)

    
    
    
    
    
    
    
    