# InvoiceLens 📦

### End-to-End Freight Cost Prediction System

Predict vendor freight costs using Machine Learning, Feature Engineering, Model Evaluation, Hyperparameter Tuning, Explainable AI (SHAP), and Cloud Deployment.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-green?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![SHAP](https://img.shields.io/badge/SHAP-Explainability-purple?style=for-the-badge)

</p>

---

## 🌐 Live Demo

**Streamlit Application**

https://invoicelens.streamlit.app

---

# 🚀 Project Overview

InvoiceLens is a production-style Machine Learning application that predicts freight costs from invoice data.

The project demonstrates the complete ML lifecycle:

✅ Data Collection

✅ Data Preprocessing

✅ Feature Engineering

✅ Model Training

✅ Model Evaluation

✅ Hyperparameter Tuning

✅ Model Explainability

✅ Model Deployment

The final system enables procurement and logistics teams to estimate freight costs before invoice processing, improving planning and budgeting decisions.

---

# 🎯 Business Problem

Freight expenses play a critical role in procurement and supply chain operations.

Manual estimation often results in:

- Inaccurate cost forecasting
- Budget overruns
- Vendor planning inefficiencies
- Operational uncertainty

InvoiceLens addresses this challenge through real-time machine learning predictions.

---

# 🏗️ System Architecture

```text
SQLite Database
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
GridSearchCV Tuning
        │
        ▼
SHAP Explainability
        │
        ▼
Model Serialization
        │
        ▼
Streamlit Application
        │
        ▼
Cloud Deployment
```

---

# 🧠 Machine Learning Pipeline

## 1️⃣ Data Collection

- SQLite Database
- Invoice Records
- Freight Cost Records

## 2️⃣ Data Preprocessing

- Data Cleaning
- Missing Value Handling
- Data Transformation
- Feature Selection

## 3️⃣ Feature Engineering

Features used:

- Quantity
- Invoice Dollar Amount

## 4️⃣ Model Training

Implemented and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

## 5️⃣ Hyperparameter Tuning

Performed using:

- GridSearchCV
- Cross Validation

Best Parameters:

```python
{
    "learning_rate": 0.05,
    "max_depth": 2,
    "n_estimators": 200
}
```

## 6️⃣ Explainable Machine Learning

Implemented:

- SHAP Values
- Feature Importance Analysis
- Model Interpretability

---

# 📊 Model Performance

## Final Selected Model → Linear Regression

| Metric | Score |
|----------|----------|
| R² Score | 97.00% |
| MAE | 24.46 |
| RMSE | 124.43 |

---

## Model Comparison

| Model | MAE | RMSE | R² Score |
|---------|---------|---------|---------|
| Linear Regression | 24.46 | 124.43 | 97.00% |
| Decision Tree | 38.12 | 138.25 | 96.30% |
| Random Forest | 30.27 | 130.63 | 96.70% |
| XGBoost | 26.96 | 154.20 | 95.40% |

---

# 🏆 Why Linear Regression Was Selected

Linear Regression achieved:

- Highest R² Score
- Lowest MAE
- Lowest RMSE
- Best Overall Generalization

Final Metrics:

```text
R² Score : 97.00%
MAE      : 24.46
RMSE     : 124.43
```

Therefore it was chosen as the production model deployed in the Streamlit application.

---

# ⚙️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Language | Python |
| Database | SQLite |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-Learn |
| Gradient Boosting | XGBoost |
| Hyperparameter Tuning | GridSearchCV |
| Explainability | SHAP |
| Visualization | Matplotlib, Seaborn |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

# ✨ Application Features

### 📈 Model Performance Dashboard

Displays:

- R² Score
- MAE
- RMSE

### 🚚 Freight Cost Prediction

User Inputs:

- Quantity
- Invoice Dollar Amount

Output:

- Predicted Freight Cost

### 📊 Business Insights

- Cost Forecasting
- Budget Planning
- Freight Optimization
- Procurement Analytics

### ☁️ Cloud Deployment

- Hosted on Streamlit Cloud
- Publicly Accessible
- Real-Time Predictions

---

# 📂 Project Structure

```text
InvoiceLens/
│
├── data/
│
├── models/
│   ├── linear_regression.pkl
│   └── tuned_xgboost.pkl
│
├── notebooks/
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   ├── hyperparameter_tuning.py
│   ├── interpretability.py
│   ├── prediction.py
│   └── main.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🖥️ Installation

Clone repository:

```bash
git clone https://github.com/bitwise-arnesh/InvoiceLens.git
```

Move into project:

```bash
cd InvoiceLens
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Training Pipeline

```bash
python src/main.py
```

---

# ▶️ Launch Streamlit Application

```bash
streamlit run app.py
```

---

# 💼 Business Impact

- Improved Freight Cost Forecasting
- Better Budget Planning
- Vendor Freight Optimization
- Data-Driven Procurement Decisions
- Reduced Manual Estimation Effort
- Faster Operational Decision-Making

---

# 🎓 Key Learning Outcomes

This project demonstrates:

- End-to-End Machine Learning Pipeline Development
- Database Integration with SQLite
- Regression Model Comparison
- Hyperparameter Optimization
- Explainable AI using SHAP
- Model Serialization using Joblib
- Streamlit Dashboard Development
- Cloud Deployment of ML Applications

---

# 👨‍💻 Author

## Arnesh Bera

Computer Science Engineering Student

### Areas of Interest

- Machine Learning
- Data Science
- Artificial Intelligence
- Generative AI

### Connect With Me

GitHub:
https://github.com/bitwise-arnesh

LinkedIn:
https://www.linkedin.com/in/arnesh-bera

---

⭐ If you found this project useful, consider giving it a star.
