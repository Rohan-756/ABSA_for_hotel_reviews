import streamlit as st
import joblib

# Load model + vectorizer
vectorizer, svm = joblib.load("./models/final_svm_model_improved.joblib")

def to_polarity(rating):
    if rating == 1:
        return "positive"
    elif rating == 0:
        return "neutral"
    else:
        return "negative"

st.title("Hotel Review Sentiment Predictor 🏨")

# User input
review = st.text_area("Enter a hotel review:")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        X = vectorizer.transform([review])
        pred = svm.predict(X)[0]
        sentiment = to_polarity(pred)
        st.success(f"⭐ Predicted Rating: {int(pred)} ({sentiment})")

