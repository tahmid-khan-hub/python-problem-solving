''' Create a nested list to store departments and their subjects.
For each department, input the number of subjects and their names.'''

courses = []

# Enter number of departments
n = int(input())

for i in range(n):
    # Enter department name
    dept = input()

    # Enter number of subjects
    m = int(input())
    subjects = []

    for j in range(m):
        sub = input() # Enter subject name
        subjects.append(sub)

    courses.append([dept, subjects])

#  example
print(courses[0][1][2])   # 3rd subject of 1st department

# Add a new subject
courses[0][1].append("Robotics")

print(courses)
