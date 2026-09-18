import streamlit as st
import pickle
import os
import numpy as np
# Load the trained model
svm_model = joblib.load(os.path.join('svm_model.pkl'))
vectorizer = joblib.load(os.path.join('Tfidf_vectorizer.pkl'))
print("Models loaded successfully!")
# App title
st.title("Sentiment Analysis App")
# User input
user_input = st.text_area("Enter your text here:")
#predict button
if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.write("Please enter some text to analyze.")
    else:
        review_vector = vectorizer.transform([user_input])
# Predict sentiment
prediction = model.predict(review_vector)
if st.button("Predict Sentiment"):
    if prediction[0] == 1:
        st.write("The sentiment is: Positive")
    else:
        st.write("The sentiment is: Negative")
