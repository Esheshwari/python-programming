import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("5ds_salaries.csv")  # Replace with the actual file path

# Step 2: Inspect the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Visualize the data distribution for the 'salary_in_usd' column using Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(df['salary_in_usd'], kde=True, color='skyblue')
plt.title('Salary Distribution (USD)')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
