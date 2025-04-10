import pandas as pd

# Example dataset (replace this with actual data from your CSV file)
data = {
    "Screen_size_inches": [15.6, 14.0, 17.3, 13.3, 12.5, 16.0, 18.4, 14.1, 19.0, 15.6, 20.0]
}

# Creating a DataFrame
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 1: Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df["Screen_size_inches"].quantile(0.25)
Q3 = df["Screen_size_inches"].quantile(0.75)
IQR = Q3 - Q1

# Step 2: Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nQ1: {Q1}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")
print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")

# Step 3: Identify outliers
outliers = df[(df["Screen_size_inches"] < lower_bound) | (df["Screen_size_inches"] > upper_bound)]
print("\nOutliers:")
print(outliers)

# Step 4: Non-outlier data
non_outliers = df[(df["Screen_size_inches"] >= lower_bound) & (df["Screen_size_inches"] <= upper_bound)]
print("\nNon-Outliers:")
print(non_outliers)
