#  Return multiple values from a function

def calculation(a, b):
    sumnumber = a+b
    subnumber = a-b
    return sumnumber,subnumber

res = calculation(40, 10)
print(res)