num = int(input("Enter Number : "))
newnum = num
reversnum = str(num)[::-1]
print(reversnum)
if num == int(reversnum):
    print("This is Palidrome Number")
else:
    print("This is Not Palidrome Number")
    