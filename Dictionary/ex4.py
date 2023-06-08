#  Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dic1=dict.fromkeys(employees,defaults)
print(dic1)