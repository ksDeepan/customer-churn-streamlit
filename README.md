📊 Customer Churn Prediction App

🚀 An interactive Streamlit web application that predicts whether a customer is likely to churn, based on key factors such as demographics, account information, and service usage.

🔗 Live Demo: Click here to try the app

✨ Features

Upload customer data (CSV) or enter details manually

Predict customer churn using a trained Machine Learning model

Real-time interactive interface built with Streamlit

Simple, lightweight, and easy to deploy

🛠️ Tech Stack

Programming Language: Python 🐍

Frameworks & Libraries:

Streamlit (frontend)

Pandas & NumPy (data processing)

Scikit-learn (machine learning)

Deployment: Streamlit Cloud

📂 Project Structure
customer-churn-streamlit/
│
├── app.py                # Main Streamlit app
├── model.pkl             # Saved ML model (if included)
├── requirements.txt      # Dependencies
├── data/                 # (Optional) Sample dataset
└── README.md             # Project documentation

⚙️ Installation (Run Locally)

Clone the repository:

git clone https://github.com/ksDeepan/customer-churn-streamlit.git
cd customer-churn-streamlit


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

📊 Dataset

This project is based on a customer churn dataset that includes features like:

Customer demographics (age, gender, region)

Subscription details (tenure, contract type, monthly charges)

Services used (internet, phone, streaming, etc.)

Note: Replace with your dataset link if public (e.g., Kaggle Telco Churn Dataset
).

🚀 Deployment

The app is deployed using Streamlit Cloud.
You can view it here 👉 Live App

📌 Future Improvements

Add support for batch predictions

Improve UI with charts & dashboards

Integrate feature importance explanation (SHAP/Plotly)

👨‍💻 Author

Deepan KS

GitHub: ksDeepan

LinkedIn: Deepan KS
