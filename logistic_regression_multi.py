# -*- coding: utf-8 -*-
"""Logistic_Regression_Multi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/170jRD_m17ak9b0d_bv0a4rZ5_-XJ54nF
"""

#using logistic regression with multiclass classification using python
import pandas as pd

dataset = pd.read_csv(r'Iris.csv')

dataset

#to display the different species in the iris dataset
dataset['Species'].unique()

#to change different species into numbers
dataset['Species'].replace({'Iris-setosa':'1', 'Iris-versicolor':'2', 'Iris-virginica':'3'} , inplace = True)

dataset

#training the model
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(dataset[['SepalLength','SepalWidth','PetalLength','PetalWidth']], dataset['Species'] , test_size=0.2)

len(x_train)

x_train

len(x_test)

x_test

#importing Logistic Regression class
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit(x_train , y_train)

lr.predict(x_test)

x_test

lr.score(x_test,y_test)

#visualizing the model
import seaborn as sns

sns.pairplot(dataset[['SepalLength','SepalWidth','PetalLength','PetalWidth','Species']] , hue='Species')