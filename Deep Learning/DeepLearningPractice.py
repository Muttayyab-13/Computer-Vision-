# -*- coding: utf-8 -*-
"""DL1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MqAUeC0AArsKejoQaD13Lof6rR5DwgmT
"""

# Import libraries

#pip install scikit-learn
#pip install tensorflow --- You should install tensorflow first
# you should have python version 3.10 or less


import pandas as pd
import numpy as np
from numpy import genfromtxt

#from google.colab import drive
#drive.mount('/content/drive')

data=genfromtxt('/content/drive/MyDrive/bank_note_data.txt',delimiter=',')
data

labels=data[:,4]
labels

features=data[:,0:4]
features

"""x=features
y=labels
"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(features,labels,test_size=0.2,random_state=0)

x_train

x_test

y_train

"""#Standardize the datset"""

#scaling

from sklearn.preprocessing import MinMaxScaler

scaler_object=MinMaxScaler()

scaler_object.fit(x_train)

scaled_x_train=scaler_object.transform(x_train)

scaled_x_test=scaler_object.transform(x_test)

scaled_x_test

scaled_x_train.max()

scaled_x_train.min()

scaled_x_test.max()

scaled_x_test.max()

"""#Building neural network"""

#pip install keras #keras==tensorflow

from keras.models import Sequential
from keras.layers import Dense

#creating model in a sequence
model=Sequential()

#neurons 5--hidden layer 1
model.add(Dense(4,input_dim=4,activation='relu'))

#neurons 2--hidden layer 1
model.add(Dense(2,activation='relu'))

#neurons 1--Output layer 1
model.add(Dense(1,activation='sigmoid'))

"""#Compile  MODEL"""

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

"""#Training the model

"""

model.fit(scaled_x_train,y_train,epochs=250,verbose=1)

#divides the data into 35 chunks,pure data set ko chunks mai
#kar ke w aur b ki values ko sahi karta
#thora thora data de kar loss check karrta take bar bar pura data na dena parhe
#step by step epoch on chunks

# 1 epochs == jab model pure data aik bar dekhta learn karta
# 35 chunks ko check karta aik epochs



"""#Prediction on unseen **Values**"""

predictions=model.predict(scaled_x_test)
predictions
#this is giving  probablities of being 1.

"""#Proper results"""

predicted_classes=np.where(predictions>0.5,1,0)
predicted_classes



"""#Evaluating the model performance"""

model.metrics_names

model.evaluate(x=scaled_x_test,y=y_test)

from sklearn.metrics import confusion_matrix,classification_report

print(classification_report(y_test,predicted_classes))

print(confusion_matrix(y_test,predicted_classes))

model.save('myfirstmodel.h5')

#.h5 == format

from keras.models import load_model

loaded_model = load_model('myfirstmodel.h5')