#  Write a program to count occurrences of all characters within a string

str1 = "Apple"
dict1={}
for i in str1:
    count = str1.count(i)
    dict1[f'{i}'] = count

print(dict1)