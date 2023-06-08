# Write a Program to extract each digit from an integer in the reverse order

num = 7536
while num > 0 :
    digit  = num % 10
    num = num // 10 
    print(digit,end= " ") 