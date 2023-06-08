#  Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_str=[]
for i in list1:
    if i:
        new_str.append(i)
        
print(new_str)