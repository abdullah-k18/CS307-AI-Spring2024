# -*- coding: utf-8 -*-
"""AbdullahBinAltaf-Lab07-19April2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YLmh7wWo-DeAHR4vrPqfxHA3ZVJSckV0
"""

import pandas as pd
df = pd.read_csv('train.csv')

df.head()

print(df.info())

print(df.describe())

print(df.isnull().sum())

df.drop("Name", axis = 1, inplace = True)
df.drop("Ticket", axis = 1, inplace = True)
df.drop("PassengerId", axis = 1, inplace = True)
df.drop("Cabin", axis = 1, inplace = True)
df.drop("Embarked", axis = 1, inplace = True)
df

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df1 = df
df1

df1 = df1.dropna(axis = 'columns')

df1 = df1.dropna(axis = 'rows')

df1

df_mean = df1.fillna(df1.mean())
df_mean

df_mean.isnull().sum()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test, = train_test_split(df1.drop('Survived', axis = 1), df1['Survived'], test_size = 0.2, random_state = 42)