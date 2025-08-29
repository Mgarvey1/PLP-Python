# Activity 2: Polymorphism Challenge
# ==============================

# Parent class: Vehicle
class Vehicle:
    def move(self):
        """
        Generic move method for any vehicle.
        This will be overridden in child classes.
        """
        return "This vehicle moves in some way."

# Child class 1: Car
class Car(Vehicle):
    def move(self):
        """
        Car moves by driving on roads.
        Overrides the parent move() method.
        """
        return "🚗 Driving on the road..."

# Child class 2: Bike
class Bike(Vehicle):
    def move(self):
        """
        Bike moves by pedaling.
        Overrides the parent move() method.
        """
        return "🚴‍♂️ Pedaling along the path..."

# Child class 3: Plane
class Plane(Vehicle):
    def move(self):
        """
        Plane moves by flying in the air.
        Overrides the parent move() method.
        """
        return "✈️ Flying through the sky..."

# ==============================
# Example usage
# ==============================

# Create instances of each vehicle
my_car = Car()
my_bike = Bike()
my_plane = Plane()

# Demonstrate polymorphism: same method name, different behavior
print(my_car.move())   # Output: 🚗 Driving on the road...
print(my_bike.move())  # Output: 🚴‍♂️ Pedaling along the path...
print(my_plane.move()) # Output: ✈️ Flying through the sky...

# ==============================
# Key Concept:
# ==============================
# Polymorphism allows objects of different classes to be treated 
# the same way while still behaving differently.
# Here, the move() method exists in all child classes but produces
# unique output for each vehicle type.
