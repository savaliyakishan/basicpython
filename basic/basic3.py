# Print characters from a string that are present at an even index numberPrint the sum of the current number and the previous number

string = str(input("Enter String : "))
for i,j in enumerate(string):
    if i % 2 == 0 :
        print(j)