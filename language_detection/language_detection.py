# -*- coding: utf-8 -*-
"""language_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RZ4C39ruXNP9mfKJtWnQMmuqtF-_0oWO
"""
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib
warnings.simplefilter("ignore")

data=pd.read_csv("Language Detection.csv")

x=data["Text"]
y=data["Language"]

data["Language"].value_counts()


le=LabelEncoder()
y=le.fit_transform(y)

data_list = []

for text in x:
       # removing the symbols and numbers
        text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
        text = re.sub(r'[[]]', ' ', text)
        # converting the text to lower case
        text = text.lower()
        # appending to data_list
        data_list.append(text)


cv=CountVectorizer()
x=cv.fit_transform(data_list).toarray()


x_train,x_test,y_train,y_test=train_test_split(x,y,shuffle=True,test_size=0.20)


model=MultinomialNB()
model.fit(x_train,y_train)


y_pred=model.predict(x_test)
print(accuracy_score(y_test,y_pred)*100)

def prediction(text):
  x=cv.transform([text]).toarray()
  lan=model.predict(x)
  lan=le.inverse_transform(lan)
  print(lan)

prediction("hellow there")

prediction("Какого черта ты делаешь")

prediction("क्या आप अंग्रेजी बोलते हैं?")


joblib.dump(model,"language_detection_model.pkl")
cv=joblib.dump(cv,"cv.pkl")
le=joblib.dump(le,"le.pkl")
