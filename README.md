# 💼 Employee Salary Predictor - Streamlit App

This is a machine learning web app that predicts whether an employee earns **>50K or <=50K salary** based on demographic and professional information. The app is built using **Streamlit**, and the model is trained on the UCI Adult dataset.

---

## 🚀 Live Demo

https://employeesalaryprediction-2ffejxaek22p5eqrryzprf.streamlit.app/

---

## 📊 Features

- Input employee attributes like age, education, workclass, hours per week, etc.
- Get instant prediction whether the salary is **above or below 50K**.
- Easy-to-use interface via Streamlit.

---

## 🧠 Machine Learning

- Model: `RandomForestClassifier` / `DecisionTreeClassifier`
- Metrics: Accuracy score, precision/recall
- Trained on cleaned and preprocessed data
- Encoded categorical variables using LabelEncoder / OneHotEncoder

---

## 📁 Project Structure
employee-salary-predictor/
│
├── app.py 
├── model.pkl 
├── label_encoder.pkl 
├── columns.pkl 
├── requirements.txt 
└── README.md 

