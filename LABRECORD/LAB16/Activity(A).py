import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("6Med.csv")  # Replace with the actual file path

# Step 2: Inspect the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Create a line plot using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["Variable"], marker='o', color='skyblue', label='Trend')
plt.title("Variable Trend Over the Years (Matplotlib)")
plt.xlabel("Year")
plt.ylabel("Variable")
plt.grid(True)
plt.legend()
plt.show()

# Step 4: Create a line plot using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x="Year", y="Variable", data=df, marker='o', color='red', label='Trend')
plt.title("Variable Trend Over the Years (Seaborn)")
plt.xlabel("Year")
plt.ylabel("Variable")
plt.legend()
plt.grid(True)
plt.show()
