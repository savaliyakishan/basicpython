# Add a list of elements to a set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

print(set(sample_list + list(sample_set)))
sample_set.update(sample_list)
print(sample_set)
