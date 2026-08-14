import pandas as pd
import matplotlib.pyplot as plt

# TASK 1 - Read the dataset into a DataFrame
countries_df = pd.read_csv(
    "Module15 - Visualization with Data Science/data/Countries Data.csv")
countries = countries_df
countries.head(3)

# TASK 2 - Extract the rows where the year is 1952
c_52 = countries.loc[countries['year'] == 1952]
print(c_52.head())

# TASK 3 - Extract the rows where the year is 2007
c_07 = countries.loc[countries['year'] == 2007]
c_07.head()

print(type(c_52))

# TASK 4 - Merge the '52 and '07 DataFrames together
c_merge = c_52.merge(c_07, left_on="country", right_on="country")
c_merge.head()

# TASK 5 - Drop both the year columns
c_merge.drop(['year_x', 'year_y'], axis=1)
c_merge.head()

# TASK 6 - Create a new column that takes the difference between the population_y and population_x column
c_merge["population_growth"] = c_merge["population_y"] - \
    c_merge["population_x"]
c_merge.head()

print(c_merge.shape)
print(type(c_merge))

# TASK 7 - Sort the values so you get back the 10 countries with the biggest population growth
c_merge = c_merge.sort_values("population_growth", ascending=False).head(10)
print(c_merge.head(10))

# TASK 8 - Plot the data
names = ["China", "India", "United States", "Indonesia", "Brazil",
         "Pakistan", "Bangladesh", "Nigeria", "Mexico", "Philippines"]
pop_grow = (c_merge["population_growth"] / 10 ** 6)

plt.figure(figsize=(15, 9))
plt.bar(names, pop_grow, width=0.6)
plt.xlabel('Country')
plt.ylabel("Population Growth (Millions)")
plt.title("Top 10 countries with the Biggest Population Growth from 1952 to 2007")
plt.xticks(rotation=45)

# TASK 9 - zip joins x and y coordinates in pairs
for x, y in zip(names, pop_grow):
    label = "({:.2f})".format(y)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha="center")

plt.show()
