# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

Bobj = Bus('kish',152,12)
print(Bobj.max_speed)
