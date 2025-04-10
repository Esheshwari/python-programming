import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("5ds_salaries.csv")  # Replace with the correct file path

# Step 2: Inspect the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Create a pair plot
sns.pairplot(df)
plt.title("Pair Plot of 5ds_salaries Dataset")
plt.show()
