#  Write a program to display all prime numbers within a range
start = 25
end = 50
list1=[]
for i in range(start,end+1):
    if i > 0:
        for j in range(2,i):
            if i % j == 0 :
                break
        else:
            list1.append(i)
print(list1)