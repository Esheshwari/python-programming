import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)
print("DataFrame from Scratch:")
print(df)

# Adding a new column 'Bonus' (10% of Salary)
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding 'Bonus' column:")
print(df)
