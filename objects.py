from main import Student
from main import Person
from main import Animals
from main import Rectangle

student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.gender)
print(student1.age)

student2 = Student()
print(student2.first_name)
print(student2.last_name)
print(student2.gender)
print(student2.age)



person1 = Person("Jane", "Female", "Single", "Pilot")
person2 = Person("Alex", "Male", "Married", "Nurse")
person3 = Person("June", "Male", "Divorced", "Driver")

print(person1.name)
print(person3.marital_status)
print(person2.gender)
print(f"Name: {person2.name}, Gender: {person2.gender}, Marital_status: {person2.marital_status}, Occupation: {person2.occupation}")
person1.salutation()
person2.salutation()
person3.salutation()

person1.display_name()
person2.display_name()
person3.display_name()

Animal1 = Animals("Lion", "Forest", 20, "Running")
Animal2 = Animals("Whale", "Ocean", 34, "Swimming")
Animal3 = Animals("Hare", "Bushes", 10, "Jumping")
Animal4 = Animals("Snake", "Trees", 25, "Slithering")

print(Animal1.name)
print(Animal3.age)
print(f"Name: {Animal2.name}, habitat: {Animal2.habitat}, age: {Animal2.age}, movement: {Animal2.movement}")
print(f"Name: {Animal4.name}, habitat: {Animal4.habitat}, age: {Animal4.age}, movement: {Animal4.movement}")


rectangle1 = Rectangle(2,3)
rectangle2 = Rectangle(4,5)
rectangle3 = Rectangle(5,6)
rectangle4 = Rectangle(7,10)

print(f"Rectangle 1: {rectangle1.display_results()}")
print(f"Rectangle 2: {rectangle2.display_results()}")
print(f"Rectangle 3: {rectangle3.display_results()}")
print(f"Rectangle 4: {rectangle4.display_results()}")



