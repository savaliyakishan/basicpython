#  Read line number 4 from the following file

with open("D:/Rejoice/Basic/inputoutput/test.txt",'r') as f:
    lines = f.readlines()
    for i,j in enumerate(lines):
        if i == 3 :
            print(j)