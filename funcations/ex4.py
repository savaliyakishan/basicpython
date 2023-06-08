# Create a function with a default argument
 
def person(name,salary=9000):
     return f"Name: {name} salary: {salary}"

print(person("kishan",10000))
print(person("xyz"))