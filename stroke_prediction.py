import streamlit as st
import pandas as pd
from joblib import load

# Load the model
model_path = 'C:\\Users\\Ecube\\sandiego\\project\\Optimized_Threshold_models\\best_XGBoost.pkl'
model = load(model_path)

def predict_stroke(data):
    df = pd.DataFrame(data, index=[0])
    probabilities = model.predict_proba(df)[0]  # Get probabilities for each class
    return probabilities[1]  # Return the probability of 'Stroke' class

# App title
st.title('Stroke Prediction App')

# Collecting user input features
input_data = {
    'gender': st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male', index=0),
    'age': st.number_input('Age', min_value=0.0, max_value=130.0, value=74.018303, step=0.000001, format="%.6f"),
    'hypertension': st.selectbox('Hypertension', options=[0, 1], index=0),
    'heart_disease': st.selectbox('Heart Disease', options=[0, 1], index=0),
    'ever_married': st.selectbox('Ever Married', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', index=1),
    'work_type': st.selectbox('Work Type', options=[0, 1, 2, 3, 4], format_func=lambda x: ['Govt_job', 'Never_worked', 'Private', 'Self-employed', 'children'][x], index=2),
    'Residence_type': st.selectbox('Residence Type', options=[0, 1], format_func=lambda x: 'Rural' if x == 0 else 'Urban', index=1),
    'avg_glucose_level': st.number_input('Average Glucose Level', min_value=55.0, max_value=300.0, value=198.550444, step=0.000001, format="%.6f"),
    'smoking_status': st.selectbox('Smoking Status', options=[0, 1, 2, 3], format_func=lambda x: ['Unknown', 'formerly smoked', 'never smoked', 'smokes'][x], index=0),
}

# Button to perform prediction
if st.button('Predict Stroke'):
    stroke_probability = predict_stroke(input_data)
    outcome_color = "red" if stroke_probability > 0.5091 else "green"
    outcome_text = "Stroke" if stroke_probability > 0.5091 else "No Stroke"
    st.markdown(f'<h2 style="color: {outcome_color};">The prediction is: {outcome_text} (Probability: {stroke_probability:.2f})</h2>', unsafe_allow_html=True)
    st.progress(int(stroke_probability * 100))  # Convert probability to percentage
