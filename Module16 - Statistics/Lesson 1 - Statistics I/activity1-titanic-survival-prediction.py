# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
data = pd.read_csv('Module16 - Statistics/data/Titanic Dataset.csv')
print(data.head(5))

# Check the datatype
print(data.dtypes)

# Check Null Values
print(data.isnull().sum())
