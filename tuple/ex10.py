# Check if all items in the tuple are the same


tuple1 = (45, 45, 45, 45)
length = len(tuple1)
for i in tuple1:
    counted = tuple1.count(i)
    if length == counted:
        print("true")
        break