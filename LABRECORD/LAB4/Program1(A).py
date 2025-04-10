# Program to read a CSV file and perform basic analysis

import pandas as pd  # Importing the pandas library for data handling

# Reading the CSV file
df = pd.read_csv("1experience.csv")  # Replace '1experience.csv' with the actual file path if needed

# 1. Display the content of the file
print("Content of the file:")
print(df)

# 2. Find the total number of rows and columns
rows, columns = df.shape
print(f"\nTotal number of rows: {rows}")
print(f"Total number of columns: {columns}")

# 3. Calculate the length of the dataframe
length = len(df)
print(f"\nLength of the dataframe: {length}")

# 4. Display the first 2 rows only
print("\nFirst 2 rows of the dataframe:")
print(df.head(2))
