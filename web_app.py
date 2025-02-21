import streamlit as st
import numpy as np
import joblib
import requests

model = joblib.load("student_performance_model.pkl")
TOGETHER_API_KEY = "4e5ed785b761e8a31e04bcd6529761f554c27030601eb1a163bb1a0dd23487fd    "

def get_study_tips(study_query):
    url = "https://api.together.xyz/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [{"role": "system", "content": "You are an AI assistant providing study advice."},
                    {"role": "user", "content": study_query}],
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"


st.title("📚 AI-Powered CGPA Predictor")
st.subheader("Enter your details to predict your CGPA.")

jee_score = st.slider("JEE Score (/100)",0,100,40)
tenth_score = st.slider("10th Score (%)",0,100,50)
twelfth_score = st.slider("12th Score (%)",0,100,60)
study_hours = st.slider("Study Hours per Week",0,50,20)
attendance = st.slider("Attendance (%)",0,100,70)
screen_time = st.slider("Avg Screen Time (hours/day)",0,24,5)

# ✅ Dropdowns for Multiple Choice Inputs
internship = st.selectbox("Have you done an Internship?", ["Yes", "No"])
extracurricular = st.selectbox("Participated in Extracurricular Activities?", ["Yes", "No"])

internship = 1 if internship == "Yes" else 0
extracurricular = 1 if extracurricular == "Yes" else 0

if st.button("Predict CGPA"):
    # Prepare input data (No Scaling Needed)
    user_data = np.array([[float(tenth_score), float(twelfth_score),
                        float(jee_score), float(study_hours), float(attendance),
                        float(screen_time), internship, extracurricular]])

    # Make prediction
    prediction = model.predict(user_data)
    st.success(f"📊 Predicted CGPA: {round(prediction[0], 2)} / 10")

    # Performance Warning
    if prediction[0] < 6:
        st.error("⚠️ Your CGPA is low! Consider increasing study hours and reducing screen time.")
        
st.subheader("AI Study Assistance")
user_query = st.text_input("Ask AI: How to improve in studies:")

if st.button("Get Study Tips"):
    if user_query:
        ai_response = get_study_tips(user_query)
        st.write("📖 **AI Advice:**", ai_response)
    else:
        st.warning("⚠️ Please enter a study-related question!")