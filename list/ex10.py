# Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

list1 = list(set(list1))
list1.remove(20)
print(list1)