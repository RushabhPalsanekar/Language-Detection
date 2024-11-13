data_list = []

# for text in x:
#        # removing the symbols and numbers
#         text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
#         text = re.sub(r'[[]]', ' ', text)
#         # converting the text to lower case
#         text = text.lower()
#         # appending to data_list
#         data_list.append(text)

# from sklearn.feature_extraction.text import CountVectorizer
# cv=CountVectorizer()
# x=cv.fit_transform(data_list).toarray()

# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x,y,shuffle=True,test_size=0.20)

# from sklearn.naive_bayes import MultinomialNB
# model=MultinomialNB()
# model.fit(x_train,y_train)

# from sklearn.metrics import accuracy_score
# y_pred=model.predict(x_test)
# print(accuracy_score(y_test,y_pred)*100)

# def prediction(text):
#   x=cv.transform([text]).toarray()
#   lan=model.predict(x)
#   lan=le.inverse_transform(lan)
#   print(lan)

# prediction("hellow there")

# prediction("Какого черта ты делаешь")

# prediction("क्या आप अंग्रेजी बोलते हैं?")
