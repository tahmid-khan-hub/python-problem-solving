'''
You are given a CSV file named employees.csv with the following data:

Name,Department,Salary,Experience
Alice,Engineering,85000,5
Bob,Marketing,60000,3
Charlie,Engineering,95000,8
David,Marketing,72000,6
Eve,HR,55000,2
Frank,HR,61000,4
Grace,Engineering,78000,3

Tasks:
1. Read the CSV file using Pandas.
2. Add a new column "Seniority" — "Junior" if Experience < 4, else "Senior".
3. Find the department with the highest average salary.
4. Display only Engineering employees with salary above the overall average salary.
'''

import pandas as pd

df = pd.read_csv("employees.csv")

df["Seniority"] = df["Experience"].apply(lambda x: "Junior" if x < 4 else "Senior")

dept_avg = df.groupby("Department")["Salary"].mean()
top_dept = dept_avg.idxmax()

overall_avg = df["Salary"].mean()
eng_high = df[(df["Department"] == "Engineering") & (df["Salary"] > overall_avg)]

print("Data with Seniority:")
print(df)

print(f"\nDepartment with Highest Average Salary: {top_dept} (${dept_avg[top_dept]:,.2f})")

print("\nEngineering Employees Above Overall Average Salary:")
print(eng_high)