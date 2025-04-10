import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace '4laptops.csv' with the actual file path)
df = pd.read_csv("4laptops.csv")

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())

# Visualizing outliers using a box plot with Matplotlib
plt.figure(figsize=(8, 5))
plt.boxplot(df['Price'], vert=False, patch_artist=True, boxprops=dict(facecolor='skyblue'))
plt.title("Box Plot of Laptop Prices (Matplotlib)")
plt.xlabel("Price")
plt.show()

# Visualizing outliers using a box plot with Seaborn
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Price'], color="skyblue")
plt.title("Box Plot of Laptop Prices (Seaborn)")
plt.xlabel("Price")
plt.show()
