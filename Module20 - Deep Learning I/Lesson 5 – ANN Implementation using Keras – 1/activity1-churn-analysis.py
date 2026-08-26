# ACTIVITY - CHURN MODELLING USING ANN - PART 1
# Create a Churn Model to predict whether a customer will exit the services or not using Keras.
# In Part-1, perform data preprocessing and prepare data for feeding into the neural network.

import pandas as pd

# TASK 1 - READ THE DATASET INTO A DATAFRAME
df = pd.read_csv("Module20 - Deep Learning I/data/Churn_Modelling.csv")

# TASK 2 - EXPLORE THE DATA
print(df.head(), "\n")

print(df.info(), "\n")

print(df.describe(), "\n")

print("Unique values of Gender column", df['Gender'].unique())
print("Unique values of Geography column", df['Geography'].unique())

# CONCLUSION
# 1. Dataset Shape - (10000, 14)
# 2. Numerical features - 11
# 3. Categorical features - 3
# 4. Null Values - 0

# TASK 3 - DATA PRE-PROCESSING
# 3.1 - LABEL ENCODING

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

df['Geography'] = encoder.fit_transform(df['Geography'])
df['Gender'] = encoder.fit_transform(df['Gender'])

print(df)

print(df.info())

# print("Unique values of Gender column", df['Gender'].unique())
# print("Unique values of Geography column", df['Geography'].unique())

# 3.2 FEATURE SELECTION - Drop the columns that are unnecessary for Neural Network training/inference
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

print("Dimensions of DataFrame after removing unnecessary features", df.shape)

# 3.3 TRAIN/TEST SPLIT
y = df.pop("Exited")
X = df

print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

# 3.4 FEATURE SCALING

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)

# ONLY transform test data (using training stats)
X_test = sc.transform(X_test) 

print(X_train)

print(X_train.describe())