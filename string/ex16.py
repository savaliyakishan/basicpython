# Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
str2=""
for i in str1.split():
    if i.isalpha():
        continue
    else:
        str2 += i    
print(str2)