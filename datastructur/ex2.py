# Remove and add item in a list

sample_list = [34, 54, 67, 89, 11, 43, 94]
element = sample_list.pop(4)
sample_list.insert(2, element)
sample_list.append(element)
print(sample_list)