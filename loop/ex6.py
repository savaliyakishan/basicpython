# Count the total number of digits in a number
n = 758962324224

lenn = 0
while n > 0:
    digit = n % 10
    n = n // 10
    lenn += 1  
print(lenn)