import streamlit as st
import pandas as pd 
import joblib


# Load trained model
model = joblib.load('salary_model.pkl')

st.header("Interactive Artificial Intelligence Salary App.")

st.markdown("Predict the estimated salary (USD) for an AI/Data related job based on selected inputs.")
st.markdown("Data Source: _www.kaggle.com_")

# Sidebar inputs
st.sidebar.header("Select Features")

# Feature inputs
job_title = st.sidebar.selectbox("Job Title", [ "AI Architect", "AI Consultant", "AI Product Manager", "AI Research Scientist", "AI Software Engineer", "AI Specialist", "Autonomous Systems Engineer", "Computer Vision Engineer", 'Data Analyst', "Data Engineer", "Data Scientist","Deep Learning Engineer", "Head of AI", "ML Ops Engineer", "Machine Learning Engineer","Machine Learning Researcher", "NLP Engineer", "Principal Data Scientist", "Research Scientist", "Robotics Engineer"          
])

experience_level = st.sidebar.selectbox("Experience Level", [
    "EN", "MI", "SE", "EX"
])

employment_type = st.sidebar.selectbox("Employment Type", [
    "FT", "PT", "CT", "FL"
])

education_level = st.sidebar.selectbox("Education Level", [
    "Associate", "Bachelor", "Master", "PhD", 
])

industry = st.sidebar.selectbox("Industry", [
    "Automotive", "Consulting", "Education", "Energy", "Finance", "Gaming", "Government", "Healthcare", "Manufacturing", "Media", "Real Estate", "Retail", "Technology", "Telecommunications", "Transportation"
    ])

remote_ratio = st.sidebar.selectbox("Remote Ratio", [
    0, 50, 100
])

company_location = st.sidebar.selectbox("Company Location", ["Australia", "Austria", "Canada", "China", "Denmark", "Finland", "France", "Germany", "India", "Ireland", "Israel", "Japan", "Netherlands", "Norway", "Singapore", "South Korea", "Sweden", "Switzerland", "United Kingdom", "United States"
])

company_size = st.sidebar.selectbox("Company Size", ['L', 'M', 'S'])


# Construct input DataFrame
input_data = pd.DataFrame({
    'job_title': [job_title],
    'experience_level': [experience_level],
    'employment_type': [employment_type],
    'company_location': [company_location],
    'company_size': [company_size],
    'remote_ratio': [remote_ratio],
    'education_required': [education_level],
    'industry': [industry],
})


# Predict salary
prediction = model.predict(input_data)[0]
formatted_salary = f"${round(prediction):,}"

# Output
st.subheader("💰 Predicted Salary (USD):")
st.success(formatted_salary)

# Optional: Show raw input
if st.checkbox("Show Input Data"):
    st.write(input_data)


