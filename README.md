⚙️ Predictive Maintenance Prediction System

A Machine Learning web application that predicts whether an industrial machine is likely to fail based on its operating conditions.

The application was developed using Python, Scikit-learn and Streamlit, with a Random Forest Classifier selected as the final deployment model.

⸻

🚀 Live Demo

Streamlit App: (Add your Streamlit Cloud URL here after deployment)

Example:

https://your-app-name.streamlit.app

⸻

📌 Project Overview

Predictive maintenance helps industries reduce unexpected machine failures by identifying potential failures before they occur.

This project develops a supervised machine learning model that predicts machine failure using machine operating parameters such as temperature, rotational speed, torque and tool wear.

The final model has been deployed using Streamlit, allowing users to enter machine details and obtain instant predictions.

⸻

📊 Dataset

Dataset: AI4I 2020 Predictive Maintenance Dataset

Features Used

* Machine Type
* Air Temperature (K)
* Process Temperature (K)
* Rotational Speed (RPM)
* Torque (Nm)
* Tool Wear (Minutes)

Target Variable

* 0 → No Machine Failure
* 1 → Machine Failure

Dataset Size:

* 10,000 observations
* 6 input features
* Binary classification

⸻

🎯 Project Objectives

* Perform Exploratory Data Analysis (EDA)
* Preprocess and clean the dataset
* Train multiple machine learning models
* Compare model performance
* Select the best-performing model
* Deploy the model using Streamlit

⸻

🤖 Machine Learning Models

The following algorithms were evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)

⸻

🏆 Final Model Performance

Metric	Value
Model	Random Forest Classifier
Training Accuracy	100.00%
Testing Accuracy	97.05%
Precision	54.64%
Recall	77.94%
F1 Score	0.6424
ROC-AUC	0.9702

The Random Forest Classifier achieved the best overall performance and was selected for deployment.

⸻

📁 Project Structure

Predictive_Maintenance_Project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── final_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
└── data/
    └── predictive_maintenance.csv

⸻

🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

⸻

⚙️ Installation

Clone the repository:

git clone https://github.com/<your-github-username>/Predictive_Maintenance_Project.git

Navigate to the project folder:

cd Predictive_Maintenance_Project

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

Install the required libraries:

pip install -r requirements.txt

⸻

▶️ Run the Application

streamlit run app.py

The application will open in your browser at:

http://localhost:8501

⸻

🖥️ Application Features

* Machine failure prediction
* User-friendly input interface
* Prediction confidence score
* Failure probability
* Download prediction report
* Simple and responsive Streamlit interface

⸻

📈 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Feature Scaling
6. Class Balancing (SMOTE)
7. Model Training
8. Hyperparameter Tuning
9. Model Evaluation
10. Streamlit Deployment

⸻

🔮 Future Improvements

* Deploy with real-time IoT sensor data
* Batch prediction using CSV uploads
* Automated maintenance recommendations
* Live equipment monitoring dashboard
* Deep Learning-based predictive maintenance models

⸻

👩‍💻 Author

Leena Gaikwad

This project demonstrates an end-to-end machine learning workflow for predictive maintenance, from data preprocessing and model development to deployment using Streamlit.