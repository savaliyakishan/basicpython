# Create a Class with instance attributes

class Vehicle:
        def __init__(self, max_speed ,mileage):
                self.max_speed = max_speed
                self.mileage = mileage
                
objclass = Vehicle(20,25)
print(objclass.max_speed)
print(objclass.mileage)