# Base class
class Car:
    def start_engine(self):
        pass
    
    def stop_engine(self):
        pass

# Derived class: BMW
class BMW(Car):
    def start_engine(self):
        return "BMW engine started"
    
    def stop_engine(self):
        return "BMW engine stopped"

# Derived class: Ferrari
class Ferrari(Car):
    def start_engine(self):
        return "Ferrari engine started"
    
    def stop_engine(self):
        return "Ferrari engine stopped"

# Function to demonstrate polymorphism
def car_engine_operations(car: Car):
    print(car.start_engine())
    print(car.stop_engine())

# Instantiate objects of BMW and Ferrari
bmw_car = BMW()
ferrari_car = Ferrari()

# Demonstrating polymorphism
print("BMW Car Operations:")
car_engine_operations(bmw_car)

print("\nFerrari Car Operations:")
car_engine_operations(ferrari_car)
