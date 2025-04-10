import pandas as pd  # Importing Pandas for data manipulation
import matplotlib.pyplot as plt  # Importing Matplotlib for visualization

# Step 1: Load the data from the CSV file
df = pd.read_csv("2Salary.csv")  # Replace with the actual file path if needed

# Step 2: Display the dataset
print("Dataset:")
print(df)

# Step 3: Analyze the distribution of employee experience
experience_mean = df['YearsExperience'].mean()
experience_median = df['YearsExperience'].median()
experience_std = df['YearsExperience'].std()

print("\nAnalysis of Employee Experience:")
print(f"Mean Experience: {experience_mean}")
print(f"Median Experience: {experience_median}")
print(f"Standard Deviation of Experience: {experience_std}")

# Step 4: Visualize the distribution of experience using a histogram
plt.hist(df['YearsExperience'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Employee Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
