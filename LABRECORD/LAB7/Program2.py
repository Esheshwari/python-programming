import pandas as pd  # Importing the Pandas library for data manipulation

# Step 1: Create a DataFrame from a list of dictionaries
data = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 70000},
    {"Product Name": "Smartphone", "Category": "Electronics", "Price": 30000},
    {"Product Name": "Table", "Category": "Furniture", "Price": 15000},
    {"Product Name": "Chair", "Category": "Furniture", "Price": 5000},
]
df = pd.DataFrame(data)

# Step 2: Add a new column for discounted price (99% of the original price)
df["Discounted Price"] = df["Price"] * 0.99

# Step 3: Display the DataFrame
print("DataFrame with Discounted Prices:")
print(df)
