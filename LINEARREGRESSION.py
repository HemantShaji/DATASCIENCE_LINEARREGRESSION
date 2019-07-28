import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
#Copy the csv file link and read it using the library pandas


data = pd.read_csv('C:\\Users\\heman\\Downloads\\student (1).zip',sep=";")
print(data.columns)
print(data.head())

data=data[["G1","G2","G3","studytime","failures","absences"]]

predict= "G3"

X= np.array(data.drop([predict],1))
Y=np.array(data[predict])

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
#Now we create a training model

linear= linear_model.LinearRegression()
#Creating a Model,we use fit and score,fit is used to train the model and score is used to test the accuracy of the model created
linear.fit(x_train,y_train)
acc= linear.score(x_test,y_test)
print(acc)

print('Coefficent: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])




