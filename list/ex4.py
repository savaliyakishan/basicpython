#  Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newlist=[]
for i in list1:
    for j in list2:
        newlist.append(i+j)
print(newlist)