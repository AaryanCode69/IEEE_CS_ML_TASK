# -*- coding: utf-8 -*-
"""MLIEEECS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13QCTw-BCyXE9LvDk0PLiGNKwxuVwCumz
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart_disease_data.csv')

df.head()

df.tail()

df['target'].value_counts()

"""1 : Defective heart
0 : Healthy Heart
"""

X = df.drop(columns = 'target',axis=1)

Y=df['target']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=23)

model = LogisticRegression()

model.fit(X_train,Y_train)

prediction_y= model.predict(X_test)

score = accuracy_score(Y_test,prediction_y)

print("The Accuracy Score is ",score)

input_data = (62,0,0,148,268,0,0,160,0,3.6,0,2,2)
arr = np.array(input_data)

prediction = model.predict(arr.reshape(1,-1))

if prediction[0] == 0:
  print("Healthy Person")
else :
  print("Not Healthy Person")