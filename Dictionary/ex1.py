# Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print({i:j for i,j in zip(keys,values)})