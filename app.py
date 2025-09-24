import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset (for retraining and encoders)
@st.cache_data
def load_data():
    df = pd.read_csv("Telco-Customer-Churn.csv")
    df.dropna(inplace=True)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

df = load_data()

# Encode categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features & target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Save feature names (important!)
feature_names = X.columns.tolist()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

# ------------------- STREAMLIT APP -------------------
st.title("📊 Customer Churn Prediction App")
st.write("Enter customer details below to predict whether they are likely to churn.")

# User Inputs
user_data = {}
for col in categorical_cols:
    user_data[col] = st.selectbox(f"{col}", encoders[col].classes_)

for col in df.drop(['Churn'] + categorical_cols, axis=1).columns:
    user_data[col] = st.number_input(f"{col}", min_value=0.0)

# Convert inputs to DataFrame
input_df = pd.DataFrame([user_data])

# Encode categorical features
for col in categorical_cols:
    input_df[col] = encoders[col].transform(input_df[col])

# Reorder columns to match training data
input_df = input_df[feature_names]

# Scale features
input_scaled = scaler.transform(input_df)

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer is **likely to churn** (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer will **stay** (Probability of churn: {prob:.2f})")
