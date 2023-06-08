# Print the sum of the current number and the previous number
print('Printing current and previous number sum in a range(10)')
num = 0
for i in range(0,10):
    sumnum = i + num 
    print(f"Current Number {i} Previous Number {num}  Sum:  {sumnum}")
    num = i