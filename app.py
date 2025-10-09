import streamlit as st
import joblib

# Load model + vectorizer
vectorizer, svm = joblib.load("./models/final_svm_model_improved.joblib")

# Function to map numeric prediction to sentiment
def to_polarity(rating):
    if rating == 1:
        return "Positive 😊"
    elif rating == 0:
        return "Neutral 😐"
    else:
        return "Negative 😢"

# Page configuration
st.set_page_config(
    page_title="Hotel Review Sentiment Predictor",
    page_icon="🏨",
    layout="centered"
)

# Header
st.markdown(
    """
    <h1 style='text-align: center; color: #4B0082;'>Hotel Review Sentiment Predictor 🏨</h1>
    <p style='text-align: center;'>Enter your hotel review and find out its sentiment!</p>
    """, unsafe_allow_html=True
)

# Input section
st.subheader("Write your review below:")
review = st.text_area("")

# Prediction button
if st.button("Predict Sentiment"):
    if not review.strip():
        st.warning("⚠️ Please enter a review before predicting.")
    else:
        # Transform review and predict
        X = vectorizer.transform([review])
        pred = svm.predict(X)[0]
        sentiment = to_polarity(pred)
        
        # Display result in a nice box
        st.markdown(f"""
        <div style='
            background-color:#D8F3DC;
            padding: 20px;
            border-radius: 10px;
            text-align:center;
            font-size: 20px;
            font-weight: bold;
            color: #2E8B57;
        '>
            Polarity Rating: {int(pred)} <br> Sentiment: {sentiment}
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:12px;'>Developed with ❤️ using Streamlit & SVM</p>", unsafe_allow_html=True)
