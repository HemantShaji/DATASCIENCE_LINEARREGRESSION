import pandas as pd
import numpy as np
from sklearn import linear_model
#Just to test the accuracy of the model we import train_test_split
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt



#There are some installed datasets in sklearn and one of them is boston dataset
from sklearn.datasets import load_boston
boston_dataset=load_boston()
print(boston_dataset.keys())

#Now load the boston dataset into pandas using pd.dataframe
boston=pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston.head()
#Doing head produces the first 5 values of the dataset.
print(boston.head())
#Its always important to see if there is any missing values in the dataset as precacution
print(boston.isnull().sum())
#in this case there arent any missing values
#now to plot visualizations we use seaborn library this step is called exploratory data analysis which is important
#we do this step before training the model

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(boston['LSTAT'])

#Now we create a correlation matrix that will measure the linear relastionship between the variables.
#the correlation matrix can be formed by using corr
correlation_matrix = boston.corr().round(2)
#annot = True to print the values inside the square
print(sns.heatmap(data=correlation_matrix, annot=True))
#From the heatmap we have to choose the variables to be chosen according to its correlation
plt.figure(figsize=(20, 5))

features = ['DIS', 'B']
target = boston['LSTAT']

for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = boston[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('LSTAT')
    plt.show()

