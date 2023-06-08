# Count all letters, digits, and special symbols from a given string


str1 = "P@#yn26at^&i5ve"
alph=""
num=""
special=""
for i in str1:
    if i.isalpha():
        alph += i
    elif i.isdigit():
        num += i
    else:
        special += i
    
print(len(alph))
print(len(num))
print(len(special))
    
    
    