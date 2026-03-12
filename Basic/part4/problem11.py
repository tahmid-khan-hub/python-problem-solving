''' You are given a CSV file named students.csv with the following data:

Name,Math,English,Science
Alice,85,78,90
Bob,70,65,72
Charlie,95,88,92
David,60,75,70

Tasks:
1. Read the CSV file using Pandas.
2. Add a new column called "Average" that contains the average marks of each student.
3. Find the student with the highest average marks.
4. Display only the students whose average marks are greater than 80.
'''

import pandas as pd

df = pd.read_csv("students.csv") # Read the CSV file
df["Average"] = (df["Math"] + df["English"] + df["Science"]) / 3

top_student = df.loc[df["Average"].idxmax()] # Find student with highest average

high_scores = df[df["Average"] > 80] # Filter students with average > 80

print("Data with Average:")
print(df)

print("\nTop Student:")
print(top_student)

print("\nStudents with Average > 80:")
print(high_scores)