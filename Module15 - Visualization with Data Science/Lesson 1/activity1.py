import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TASK 1 - Read data from CSV file
dataset_path = "Module15 - Visualization with Data Science/data/country_vaccinations.csv"
df = pd.read_csv(dataset_path)

# TASK 2 - Display first 10 rows
print(df.head(10))

# TASK 3 - Check for any null values in each column
print(df.isnull().any())

# TASK 4 - Visualize missing values using a heatmap (optimize by using a subset)
# Taking the first 100 rows for better performance
subset = df.iloc[:200, :]

plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="gray")
plt.show()

# TASK 5 - Drop rows where all values are NaN
df.dropna(how="all")

# TASK 6 - Fill missing values using backward fill method
df.bfill()

# TASK 7 - Interpolate missing values
numeric_cols = df.select_dtypes(include=['number']).columns
print(df[numeric_cols].interpolate())

# TASK 8 - Drop all rows with any NaN values
df_dropped = df.dropna()

print(df_dropped)
