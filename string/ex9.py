# Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
num = 0
length = ''
for i in str1:
    if i.isdigit():
        num += int(i)
        length += i

print(num)
print(num / len(length))