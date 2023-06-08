# Create a new string made of the first, middle, and last characters of each input string
 
# s1 = "America"
# s2 = "Japan"

# print(s1[0]+s2[0]+s1[int(len(s1) / 2)]+s2[int(len(s2) / 2)]+s1[-1]+s2[-1])


# Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"
newlowe = ""
newuper = ""
for i in str1:
    if i.islower():
        newlowe += i
    if i.isupper() :
        newuper += i   
print(newlowe+newuper)