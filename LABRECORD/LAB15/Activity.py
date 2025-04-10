import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace '6MedLas.csv' with the actual path of your CSV file
df = pd.read_csv("6MedLas.csv")

# Step 2: Calculate the correlation matrix
correlation_matrix = df.corr()

# Step 3: Visualize the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
