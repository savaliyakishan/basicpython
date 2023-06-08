# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
newlist=[]
for i,j in zip(list1,list2):
    newlist.append(i+j)
print(newlist)