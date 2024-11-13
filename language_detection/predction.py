import joblib

model=joblib.load("language_detection_model.pkl")
cv=joblib.load("cv.pkl")
le=joblib.load("le.pkl")


def prediction(text):
    x=cv.transform([text]).toarray()
    lang=model.predict(x)
    lang=le.inverse_transform(lang)
    print(lang)


prediction("hellow there")
prediction("क्या आप अंग्रेजी बोलते हैं?")
prediction("Какого черта ты делаешь")