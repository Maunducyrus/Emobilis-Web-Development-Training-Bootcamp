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

class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def display_name(self):
        return f"{self.name} is {self.age} years old"

class Manager(Employee):
    def __init__(self, name, age, salary, gender, education_level):
        super().__init__(name, age, salary, gender)
        self.education_level = education_level

class Developer(Employee):
    def __init__(self, name, age, salary, gender, prog_language):
        super().__init__(name, age, salary, gender)
        self.prog_language = prog_language

class SalaryEmployee(Employee):
    def __init__(self, name, age, salary, gender, monthly_salary):
        super().__init__(name, age, salary, gender)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary + self.salary

class HoursEmployee(Employee):
    def __init__(self, name, age, salary, gender, hours_worked, hourly_rate):
        super().__init__(name, age, salary, gender)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return (self.hourly_rate * self.hours_worked) + self.salary

class commissionEmployee(SalaryEmployee):
    def __init__(self, name, age, salary, gender, monthly_salary, commission):
        super().__init__(name, age, salary, gender, monthly_salary)
        self.commission = commission

        def calculate_payroll(self):
            fixed = super().calculate_salary()
            return fixed + self.commission

#create a parent class bank account which represents a bank account
# with its respective attributes
#create a deposit method that manages the deposit actions
#create a withdrawal method which manages withdrawal actions
#create a bank fees method that applies bank fees percentage of
# 5% on the balance in account
#create display method to display account details
#NB:ensure the parent class has at least 2 child classes

class BankAccount:
    def __init__(self, account_number, account_owner, balance=0):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: {self.balance}")
        else:
            print("Withdraw amount must be greater than zero")

    def bank_fees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fees is ${fees}. New balance: {self.balance}")

    def display(self):
        print(f"Account number: {self.account_number}")
        print(f"Account owner: {self.account_owner}")
        print(f"Balance: {self.balance}")

# child class for savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest} Bank balance is ${self.balance}")


# 2nd child class
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: {self.balance}")
        else:
            print("Withdraw amount must be greater than zero")


# Create a Vehicle class in Python with a start() method that prints 'Vehicle is starting.'
# Then, create two subclasses, Car and Bike, where each has an overridden start() method that prints specific messages.
# Test both to see how method overriding works in Python.


# Parent class
class Vehicle:
    def Start(self):
        print("Vehicle is starting")

# subclass car
class Car(Vehicle):
    def Start(self):
        print("Car is starting")

# subclass Bike
class Bike(Vehicle):
    def Start(self):
        print("Bike is starting")


# Write a Device class in Python with an init() method that takes brand
# and year as parameters. Then create a Phone subclass that inherits Device and
# adds a new attribute model. Use the super() function to call the Device initializer from
# the Phone class. Test it by creating a Phone object and printing out all attributes.

# main class
class Device:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# minor class phone
class Phone(Device):
    def __init__(self, brand, year, model):
        # calling the parent class initializer
        super().__init__(brand, year)
        self.model = model










