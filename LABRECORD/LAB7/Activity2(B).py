import pandas as pd  # Importing the Pandas library for data manipulation

# Example dataset (replace with actual dataset or read from file)
data = {
    "Name": ["Alice", "Bob", "Charlie", None, "David", "Alice"],
    "Age": [25, 30, None, 22, 40, 25],
    "City": ["New York", None, "London", "Tokyo", None, "New York"]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Fill null values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Not Specified", inplace=True)

print("\nDataset After Filling Null Values:")
print(df)

# Drop duplicates
df = df.drop_duplicates()

print("\nDataset After Dropping Duplicates:")
print(df)
