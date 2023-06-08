# Display Fibonacci series up to 10 terms
n = 0
n1 = 1
n2 = n + n1
for i in range(2,20):
    print(n2)
    n = n1
    n1 = n2
    n2 = n + n2