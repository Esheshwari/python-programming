import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler

# Step 1: Load the dataset
# Replace '3Salary_Data.csv' with the actual file path
df = pd.read_csv("3Salary_Data.csv")
print("Original Dataset:")
print(df)

# Step 2: Apply Normalizer
normalizer = Normalizer()
normalized_data = normalizer.fit_transform(df[['Salary', 'YearsExperience']])
normalized_df = pd.DataFrame(normalized_data, columns=['Salary_Normalized', 'YearsExperience_Normalized'])

print("\nData After Normalization:")
print(normalized_df)

# Step 3: Apply MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['Salary', 'YearsExperience']])
scaled_df = pd.DataFrame(scaled_data, columns=['Salary_Scaled', 'YearsExperience_Scaled'])

print("\nData After Min-Max Scaling:")
print(scaled_df)
