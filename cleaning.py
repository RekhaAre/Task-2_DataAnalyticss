import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/sales.csv")

# Check missing values
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Order Date column to date format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create new column
df["Year"] = df["Order Date"].dt.year

# Save cleaned dataset
df.to_csv("../output/cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully")