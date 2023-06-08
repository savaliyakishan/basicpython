# Create a Python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
newlist=[]
for i in first_list:
    if i*i in second_list:
        newlist.append((i,i*i))
print(newlist)