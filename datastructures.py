# data structures types
from random import setstate

# 1. lists
# employees = ['John', 'Joseph', 'Joan', 'Peter', 334]
#
# print(employees[0])
# print(employees[1:4])
# employees[2] = 'Andrew'
# print(employees)
# employees.append('Jack')
# print(employees)
# employees.insert(2, 'Cyrus')
# print(employees)
# employees.extend(['Kim', 'James', 'Clement'])
# print(employees)

# 2. tuples
# languages = ('Python', 'Java', 'Kotlin')
# print(languages)
# print(languages[1])
# print(languages[1:4])

# languages[2] = 'php'
# print(languages)
# marks = (200, 300, 400, 500)
# print(marks)
# print(max(marks))
# print(min(marks))
# print(sum(marks))

# 3. sets
# students = {'John', 'Ann', 'Carol', 'Jovial'}
# print(students)
# if 'John' in students:
#     print('John is present in students')
# else:
#     print('John is not present in students')
#     students.add('Vivian')
#     print(students)
#     students.update({'Maundu', 'Cruise'})
#     print(students)
#     students.remove('Maundu')
#     print(students)
#
# # 4. dictionary
# books={
#     'title': 'The book',
#     'author': 'Joe Doe',
#     'publisher': 'Kenya institute',
#     'year published': 2000,
# }
# print(books)
# print(books['publisher'])
# books['cover_color'] = 'blue'
# print(books)
#
# if 'cover_color' in books:
#     print(books['cover_color'])
# else:
#     print(books['Not Present'])

    # Create a random dictionary with more than 5 items and query
    # the existence of any of the items
good_importation={
    'Cars': 'japan',
    'Radio': 'China',
    'Television': 'Europe',
    'Machinery': 'Netherlands',
    'Metallics': 'Korea',
    'Plastics': 'Spain',
}
print(good_importation)
if 'Radio' in good_importation:
    print(good_importation['Radio'])
else:
    print(good_importation['Radios not manufactured in China'])


if 'Cars' in good_importation:
    print(good_importation['Cars'])

    good_importation['Metallics'] = 'Japan'
    print("Updated dictionary:", good_importation)

    good_importation['Furniture'] = 'Italy'
    print("Dictionary after adding 'Furniture':", good_importation)

    # using user inputs take 4 inputs and perform logical operations
    # using the operator 'and' to compare
    input1 = input("Enter you first value: ").lower() == "true"
    input2 = input("Enter you second value: ").lower() == "true"
    input3 = input("Enter you third value: ").lower() == "true"
    input4 = input("Enter you fourth value: ").lower() == "true"

    response1 = input1 and input2
    response2 = input3 and input4
    final_response = response1 and response2

    print("Result of {input1} and {input2} is: {result1}")