# Remove special symbols / punctuation from a string
import string

str1 = "/*Jon is @developer & musician"
newstr = str1.translate(str.maketrans('','',string.punctuation))
print(newstr)