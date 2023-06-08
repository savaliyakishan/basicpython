# Remove duplicates from a list and create a tuple and find the minimum and maximum number


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_tuple = tuple(set(sample_list))
print(min(sample_tuple))
print(max(sample_tuple))