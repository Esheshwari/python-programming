# Program to analyze a CSV file containing years of experience

import pandas as pd  # Importing pandas for data handling

# Reading the CSV file
df = pd.read_csv("years_experience.csv")  # Replace 'years_experience.csv' with the actual file name or path

# 1. Display the last 3 rows only
print("Last 3 rows of the dataframe:")
print(df.tail(3))

# 2. Display the description and information of the dataframe
print("\nDescription of the dataframe:")
print(df.describe())

print("\nInformation about the dataframe:")
print(df.info())

# 3. Display the column names
print("\nColumn names in the dataframe:")
print(df.columns.tolist())
