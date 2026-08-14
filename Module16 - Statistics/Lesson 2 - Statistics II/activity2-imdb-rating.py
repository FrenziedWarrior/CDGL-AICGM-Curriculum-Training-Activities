# **Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
data = pd.read_csv('Module16 - Statistics/data/IMDB Dataset.csv')

print(data.head(5))

# Check Null Values
print(data.isnull().sum())

"""**No null values present -**

#### **Plot Histogram for feature Runtime**
"""

plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

"""#### **Plot Histogram for feature IMDB_Rating**"""

plt.hist(data['IMDB_Rating'])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.show()

"""#### **Define parameter bins_runtime for feature Runtime and plot histogram for it**"""

print(data['Runtime'].unique())

bins_time = np.arange(80, 230, 10)
plt.hist(data['Runtime'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

"""#### **Define parameter bins_rating for feature IMDB_Rating and plot histogram for it**"""

print(data['IMDB_Rating'].unique())

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_rating, color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)
plt.show()
