import pandas as pd

# Example Dataset 1 for GroupBy operation
data1 = {
    "Department": ["HR", "Finance", "IT", "HR", "IT"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Salary": [50000, 60000, 70000, 55000, 65000]
}
df1 = pd.DataFrame(data1)

# Example Dataset 2 for merging and joining
data2 = {
    "Department": ["HR", "Finance", "IT", "Marketing"],
    "Location": ["New York", "London", "San Francisco", "Tokyo"]
}
df2 = pd.DataFrame(data2)

# Example Dataset 3 for concatenation
data3 = {
    "Role": ["Manager", "Analyst", "Developer", "Recruiter", "Engineer"]
}
df3 = pd.DataFrame(data3)

# 1. GroupBy operation (Median of Salary by Department)
grouped_df = df1.groupby("Department").median()
print("GroupBy (Median Salary by Department):")
print(grouped_df)

# 2. Merging the DataFrames (Outer Join)
merged_df = pd.merge(df1, df2, on="Department", how="outer")
print("\nMerged DataFrame (Outer Join):")
print(merged_df)

# 3. Joining DataFrames (Joining roles into df1)
joined_df = df1.join(df3)
print("\nJoined DataFrame:")
print(joined_df)

# 4. Concatenating DataFrames horizontally
concat_df = pd.concat([df1, df2], axis=1)
print("\nConcatenated DataFrame (Horizontally):")
print(concat_df)
