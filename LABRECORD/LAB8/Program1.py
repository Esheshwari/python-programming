import pandas as pd  # Importing the Pandas library

# Step 1: Load the data from the CSV file
df = pd.read_csv("2Salary.csv")  # Replace with the actual file path if needed

# Step 2: Display the dataset
print("Dataset:")
print(df)

# Step 3: Calculate central tendencies
mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()

print("\nCentral Tendencies:")
print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")

# Step 4: Calculate dispersion measures
variance_salary = df['Salary'].var()
std_dev_salary = df['Salary'].std()

print("\nDispersion Measures:")
print(f"Variance of Salary: {variance_salary}")
print(f"Standard Deviation of Salary: {std_dev_salary}")
