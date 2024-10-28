# functions - blocks of codes that perform a specific task
def my_function():
    print("Hello, Hope you are well!")
    print("Hello, Hope you are well!")
    print("Hello, Hope you are well!")
    print("Hello, Hope you are well!")


my_function()
my_function()

def my_func():
    name="ROBERRT"
    print(name)
my_func()

def my_func2(name):
    print(name)

my_func2("Felix")
my_func2("Laura")
my_func2("Joseph")

def concate(first_name):
    print("Hello " + first_name + ", how are you ?")
    print(f"Hello  {first_name}, how are you ?")

concate("Maundu")
concate("Bob")

def concate2(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}, you are {age} years old ")

concate2("Maundu", "Cyrus", 25)


# Create a function that two numbers and performs summation and
# displays the output
# def sum(num1, num2):
#     print(num1 + num2)
#     print(f"The sum of {num1} and {num2} is {num1 + num2}")
 # sum(4, 2)

def multiply(num1, num2):
    multiplier = num1 * num2
    return multiplier
print(multiply(10, 20))

def age_calc(current_age):
    new_age = current_age - 10
    return new_age
print(age_calc(21))

# Conditional statements in a function
def school(name, age):
    if age >= 5 and age <= 10:
        return f"{name} Your are {age} years old belong to lower primary"
    elif age >= 10 and age <= 15:
        return f"{name} Your are {age} years old belong to upper primary"
    elif age > 15:
        return f"{name} Your are {age} years old belong to senior secondary"

    else:
        return f"{name} Your are {age} years old and you are underage"

print(school("Joseph", 13))
print(school("Ann", 4))
print(school("Alex", 17))

# Assignment
# create a function called greet that takes a persons name as an
# argument and returns a greeting message. If the name is 'Alice'
# or 'bob' it returns a personalised greetings, for any other name
#     it should return a personal greeting

def greet(name):
    if name == 'Alice':
        return "Hello Alice! feel welcomed!"
    elif name == 'Bob':
        return "Hello Bob! See you next time!"
    else:
        return "Pleasure to meet you"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Cyrus"))


# write a python program that finds a maximum of three numbers
def max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
number3 = float(input("Enter your third number: "))

max_value = max(number1, number2, number3)
print(f"The maximum of the three numbers is: {max_value}")

# create a python function that sums all numbers in a list
def sum_list(numbers):
    return sum(numbers)

# Example usage
num_list = [1, 2, 3, 4, 5, 6]
result = sum_list(num_list)
print(f"The sum of the numbers in the list is: {result}")



