# Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
div = int(len(sample_list) / 3)

start = 0
newend = div
for i in range(3):
    print(sample_list[slice(start,newend)])
    start = newend
    newend += div