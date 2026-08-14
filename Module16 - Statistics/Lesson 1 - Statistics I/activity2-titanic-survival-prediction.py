# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Module16 - Statistics/data/Titanic Dataset.csv')

print(data.head())

"""####**Mean Value of Age and Fare**"""

# Mean Value of age
mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is - ", mean_age)

# Mean Value of Fare
mean_fare = np.mean(data['Fare'])
print("Mean Fare is - ", mean_fare)
