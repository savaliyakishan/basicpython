# Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

print(sorted(tuple1,key= lambda a : a[1]))