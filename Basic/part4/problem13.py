''' Find any CSV dataset of your choice (e.g., from Kaggle, or any public source) that
has at least 4 columns and 50 rows. Load it into a Pandas DataFrame and
complete all of the following:
a. Display the last 5 rows, and use .info() and .describe() to summarize the
data.
b. Select and display any 2 columns of your choice.
c. Filter the data using a condition on a numeric column (e.g., show only rows
where a value is above a certain threshold). Write a comment explaining
why you chose that filter.
d. Use groupby() on a categorical column and apply an aggregate function
(e.g., .mean(), .sum(), or .count()) to a numeric column. Explain what the
result tells you in a comment. '''

import pandas as pd

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# ── (a) ──────────────────────────────────────────────────────
print("=== Last 5 Rows ===")
print(df.tail())

print("\n=== Dataset Info ===")
df.info()

print("\n=== Statistical Summary ===")
print(df.describe())

# ── (b) ──────────────────────────────────────────────────────
print("\n=== Selected Columns: gender and math score ===")
print(df[["gender", "math score"]])

# ── (c) ──────────────────────────────────────────────────────
# Threshold of 80 isolates top ~20% of students — high achievers.
high_scorers = df[df["math score"] > 80]
print("\n=== Students with Math Score > 80 ===")
print(high_scorers)
print("\nTotal high scorers:", len(high_scorers))

# ── (d) ──────────────────────────────────────────────────────
# Grouping by test prep status to measure its impact on scores.
# Mean of binary Survived-like columns gives a proportion/rate.
print("\n=== Average Scores by Test Preparation Course ===")
result = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean().round(2)
print(result)