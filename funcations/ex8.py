#   Generate a Python list of all the even numbers between 4 to 30

def evennumber(startnu,stopnum):
    list1=[]
    for i in range(startnu,stopnum):
        if i % 2 == 0:
            list1.append(i)
    return list1
print(evennumber(4, 30))