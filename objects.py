from main import Student
from main import Person
from main import Animals
from main import Rectangle
from main import Employee
from main import Manager
from main import  Developer
from main import SalaryEmployee
from main import HoursEmployee
from main import commissionEmployee
from main import SavingsAccount
from main import BankAccount
from main import CurrentAccount
from main import Vehicle
from main import Car
from main import Bike
from main import Phone

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

employee1 = Employee("Jane", "23", 200000, "Female")
manager1 = Manager("Jones", 34, 200000, "Male", "Masters")
developer1 = Developer("Patrick", 23, 200000, "Male", "Kotlin")
salaryemployee1 = SalaryEmployee("Alex", 43, 200000,"Female", 50000)
hoursemployee1 = HoursEmployee("Susan", 43, 200000,"Female", 5, 1000)
# commissionemployee1 = commissionEmployee("Gillian", 43, 200000, "Female", 40000, )

print("\n")

print(manager1.display_name())
print(developer1.display_name())
print(salaryemployee1.display_name())
print(hoursemployee1.display_name())

print(salaryemployee1.calculate_salary())
print(hoursemployee1.calculate_payment())

# print(commissionemployee1.calculate_payroll())

savings1 = SavingsAccount("090034567823", "Cyrus Maundu", 2000)
savings1.display()
savings1.deposit(500)
savings1.withdraw(1000)
savings1.apply_interest()
savings1.bank_fees()
savings1.display()

print("\n")

savings2 = SavingsAccount("0900235363", "Alex Kosgei", 700)
savings2.display()
savings2.deposit(300)
savings2.withdraw(100)
savings2.apply_interest()
savings2.bank_fees()
savings2.display()

print("\n")

# Testing the overiding of classes and methods
vehicle1 = Vehicle()
car1 = Car()
bike1 = Bike()

Vehicle.Start(vehicle1)
Car.Start(car1)
Bike.Start(bike1)

print("\n")

# Testing the phone class
phone1 = Phone("Android", 2023, "Itel A05")

# if you want to print all attributes of the phone object
print(f"Phone Brand is: {phone1.brand}")
print(f"The year phone was published: {phone1.year}")
print(f"Phone Model is: {phone1.model}")





