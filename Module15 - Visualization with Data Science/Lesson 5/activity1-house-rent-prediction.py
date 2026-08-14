import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

house_df = pd.read_csv(
    "Module15 - Visualization with Data Science/data/USA_Housing.csv")

print(house_df.head())

print(house_df.columns)

print(house_df.info())

sns.pairplot(house_df)
plt.show()

sns.heatmap(house_df.corr(numeric_only=True), annot=True)
plt.show()
