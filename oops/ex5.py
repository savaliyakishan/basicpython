# Define a property that must have the same value for every class instance (object)

class Vehicle:
    
    color = "white"   
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
vobj = Vehicle("kk", 12, 25)
print(vobj.color)