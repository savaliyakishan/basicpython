# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str=[]
for i in str_list:
    if i:
        new_str.append(i)
        
print(new_str)