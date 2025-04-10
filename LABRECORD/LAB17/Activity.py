import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("ds_salaries.csv")  # Replace with the actual path to your file

# Step 2: Inspect the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Visualize the relationship using a bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x="JobTitle", y="Salary", data=df, ci=None, palette="Blues_d")
plt.title("Average Salary by Job Title")
plt.xlabel("Job Title")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
