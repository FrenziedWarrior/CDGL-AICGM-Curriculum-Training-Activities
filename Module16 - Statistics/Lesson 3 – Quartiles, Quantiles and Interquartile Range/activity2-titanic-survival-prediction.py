# **Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
data = pd.read_csv('Module16 - Statistics/data/Titanic Dataset.csv')

print(data.head(5))

"""####**Check Null Values**"""

print(data.isnull().sum())

"""**Null values present in Cabin -**

#### **Boxplot of Feature Age and Pclass**
"""

plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()
