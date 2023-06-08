# Check file is empty or not

with open("D:/Rejoice/Basic/inputoutput/test1.txt",'r') as f:
    if len(f.readlines()) == 0:
        print('file is empty')