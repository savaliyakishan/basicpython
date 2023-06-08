# Use a loop to display elements from a given list present at odd index positions
list1=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2=[] 
for i,j in enumerate(list1):
    if i % 2 != 0:
        list2.append(j)
print(list2)