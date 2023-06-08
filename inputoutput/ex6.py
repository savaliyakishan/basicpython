#Accept numbers from a user

file = open('D:/Rejoice/Basic/inputoutput/test.txt','r')
n = 0
for i in file.readlines():
    n += 1
    if n == 5:
        pass
    else:
        print(i)
        