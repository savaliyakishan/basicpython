# Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l1odd = l1[1::2]
print(l1odd)
l2even = l2[0::2]
print(l1odd + l2even)