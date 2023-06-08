# Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

num = 0
n = 5
number = 2
for i in range(n):
    num += number
    number = number * 10  + 2
print(num)