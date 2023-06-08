# Count the occurrence of each element from a list

dic1={}
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
for i in sample_list:
    length = sample_list.count(11)
    dic1[f'{i}']=length
print(dic1)