class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Animal:
    def move(self):
        print("Moving...")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

# Testing Polymorphism
def test_move(movable):
    movable.move()

# Create objects
car = Car()
plane = Plane()
dog = Dog()
bird = Bird()


test_move(car)     # Output: Driving 🚗
test_move(plane)   # Output: Flying ✈️
test_move(dog)     # Output: Running 🐕
test_move(bird)    # Output: Flying 🐦
