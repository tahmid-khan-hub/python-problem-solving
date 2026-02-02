''' Write a program that takes 'n' student names and their corresponding course codes as input. '''

student_records = []
formatted_names = []

n = int(input()) # number of students

for i in range(n):
    name = input() # student name
    course = input() # course code
    student_records.append([name, course])

for record in student_records:
    formatted_names.append(record[0].title()) # Capitalize names

print(formatted_names)
