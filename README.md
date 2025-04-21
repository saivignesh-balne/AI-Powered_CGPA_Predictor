**AI-Powered CGPA Predictor**  
*A machine learning tool that predicts academic performance and provides AI-powered study guidance.*

---

## **Features**  
📊 **CGPA Prediction**: Forecasts future grades using ML models  
💬 **Study Advisor Chatbot**: Get personalized study tips (ask about time management, subject help, etc.)  
📈 **Performance Analysis**: Identifies your strongest/weakest subjects  
📁 **Data Import**: Works with CSV/Excel academic records  
🎯 **Actionable Insights**: Recommends improvement strategies  

---

## **Tech Stack**  
- **ML Models**: Scikit-learn (Random Forest)  
- **Chatbot**: NLP with Transformers  
- **Backend**: Python  
- **Frontend**: Streamlit  

---

## **Installation**  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/saivignesh-balne/AI-Powered_CGPA_Predictor.git  
   cd AI-Powered_CGPA_Predictor  
   ```  

2. **Set up environment**:  
   ```bash  
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # Linux/Mac
   ```  

3. **Install packages**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## **Usage**  
1. **Run the app**:  
   ```bash  
   streamlit run app.py  
   ```  
2. **Choose mode**:  
   - *Prediction Mode*: Upload academic records  
   - *Chatbot Mode*: Ask for study advice (e.g., "How to improve my calculus grades?")  

---

## **Data Format**  
Required CSV columns:  
- `Semester_Grades` (e.g., [8.5, 7.0, 9.2])  
- `Attendance_Percentage`  
- `Weekly_Study_Hours`  
- `Previous_CGPA`  

---

## **Chatbot Commands**  
Try asking:  
- "Create a 2-week exam plan for Data Structures"  
- "How many hours should I study daily?"  
- "Ways to improve programming grades"  

---

## **Development**  
To contribute:  
1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/chatbot-upgrade`)  
3. Commit changes (`git commit -m "Add chatbot commands"`)  
4. Push to branch (`git push origin feature/chatbot-upgrade`)  
5. Open a PR  
