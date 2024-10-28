class Student:
    first_name = "Annastacia"
    last_name = "Mutheu"
    gender = "Female"
    age = 24

class Person:
    def __init__(self, name, gender, marital_status, occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salutation(self):
        print(f"Good afternoon {self.name}, you are {self.marital_status}")

    def display_name(self):
        print(f"Your name is {self.name}")

# Create a class that enables instatiation(creating objects)
# of variesties of animals. create 4 objects(animals)

class Animals:
    def __init__(self, name, habitat, age, movement):
        self.name = name
        self.habitat = habitat
        self.age = age
        self.movement = movement

# create a rectangle class that takes in length and width, create
# a perimeter method, area method and a method that displays the
# length, width, perimeter and area. create 4 objects

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display_results(self):
        print(f"length: {self.length}")
        print(f"width: {self.width}")
        print(f"perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")

