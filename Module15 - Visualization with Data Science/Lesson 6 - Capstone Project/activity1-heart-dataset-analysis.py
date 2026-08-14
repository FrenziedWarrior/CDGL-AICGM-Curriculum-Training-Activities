import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("Module15 - Visualization with Data Science/data/heart.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.describe())

print(df.isnull().sum())

print(df.info())

# TASK 1 - Histogram
df.hist(figsize=(12, 12), layout=(5, 3))

# TASK 2 - Box Plot & Whisker Plot
df.plot(kind="box", subplots=True, layout=(5, 3), figsize=(12, 12))

# TASK 3 - Bar Plot
sns.barplot(data=df, x="sex", y="chol", hue="target", palette="spring")

# TASK 4 - Display value counts for sex column
print(df["sex"].value_counts())

# TASK 5 - Display value counts for target column
print(df["target"].value_counts())

# TASK 6 - Display value counts for thal column
print(df["thal"].value_counts())

# TASK 7 - Correlation Heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(df.corr(), annot=True, cmap="terrain")
plt.show()

# TASK 8 - Count Plot for sex vs target
sns.countplot(x="sex", data=df, palette="husl", hue="target")
plt.show()

# TASK 9 - Count Plot for target
sns.countplot(x="target", data=df, palette="BuGn")
plt.show()

# TASK 10 - Count Plot for ca vs target
sns.countplot(x="ca", data=df, hue="target")
plt.show()
