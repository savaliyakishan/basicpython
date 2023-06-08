# Create a mixed String using the following rules


s1 = "Abc"
s2 = "Xyz"
lengths1 = len(s1)
lengths2 = len(s2)

length = lengths1 if lengths1 > lengths2 else lengths2
newstr = ""
s2 = s2[::-1]
for i in range(length):
    if i < lengths1:
        newstr = newstr + s1[i]
    if i < lengths2:
        newstr = newstr + s2[i]
print(newstr)
