import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace '5ds_salaries.csv' with the actual file path)
df = pd.read_csv("5ds_salaries.csv")  # Ensure the file contains the columns you want to analyze

# Inspect the dataset
print("Dataset Preview:")
print(df.head())

# Create a scatter plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(df['YearsExperience'], df['Salary'], color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Relationship Between Salary and Years of Experience (Matplotlib)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Create a scatter plot using Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='red', s=100, alpha=0.7)
plt.title('Relationship Between Salary and Years of Experience (Seaborn)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.show()
