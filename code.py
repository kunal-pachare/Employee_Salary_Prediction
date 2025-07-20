import streamlit as st
import pickle
import pandas as pd

# Load trained model and encoders
model = pickle.load(open('model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

# App title
st.title("💼 Employee Salary Prediction App")
st.write("Enter employee details to predict whether salary is >50K or <=50K.")

# Input fields for the user
def user_input():
    age = st.number_input("Age", min_value=17, max_value=90, step=1)
    workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 
                                           'Local-gov', 'State-gov', 'Without-pay'])
    education = st.selectbox("Education", ['Bachelors', 'HS-grad', '11th', 'Masters', '9th',
                                           'Some-college', 'Assoc-acdm', 'Assoc-voc', '7th-8th',
                                           'Doctorate', 'Prof-school'])
    marital_status = st.selectbox("Marital Status", ['Married-civ-spouse', 'Divorced', 'Never-married',
                                                     'Separated', 'Widowed', 'Married-spouse-absent'])
    occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales',
                                             'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners',
                                             'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving'])
    hours_per_week = st.slider("Hours per Week", 1, 99, 40)
    native_country = st.selectbox("Native Country", ['United-States', 'Mexico', 'Philippines', 'Germany', 'India', 'Other'])

    # Prepare the input as a dataframe
    data = {
        'age': age,
        'workclass': workclass,
        'education': education,
        'marital-status': marital_status,
        'occupation': occupation,
        'hours-per-week': hours_per_week,
        'native-country': native_country
    }

    return pd.DataFrame([data])

# Take input
input_df = user_input()

# Preprocess input
df_encoded = pd.get_dummies(input_df)
df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

# Predict button
if st.button("Predict Salary"):
    prediction = model.predict(df_encoded)[0]
    prediction_label = label_encoder.inverse_transform([prediction])[0]
    
    st.success(f"Predicted Salary Category: **{prediction_label}**")
