# InvoiceLens

### End-to-End Freight Cost Prediction System

Predict vendor freight costs using machine learning, feature engineering, model evaluation, hyperparameter tuning, explainability techniques, and cloud deployment.

**Live Demo:** https://invoicelens.streamlit.app

---

## Project Overview

InvoiceLens is an end-to-end Machine Learning project designed to predict freight costs from invoice data.

The project demonstrates the complete machine learning lifecycle:

1. Data Extraction from SQLite Database
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Hyperparameter Tuning
7. Model Explainability using SHAP
8. Model Serialization
9. Interactive Web Application Development
10. Cloud Deployment

The final solution enables procurement and logistics teams to estimate freight costs before invoice processing, supporting budgeting and operational decision-making.

---

## Business Problem

Freight expenses are a significant component of procurement and supply chain operations.

Manual estimation often leads to:

- Cost forecasting inaccuracies
- Budget overruns
- Vendor planning inefficiencies
- Increased operational uncertainty

InvoiceLens addresses this problem by providing real-time freight cost predictions based on invoice characteristics.

---

## Project Architecture

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
Hyperparameter Tuning
       │
       ▼
SHAP Interpretability
       │
       ▼
Model Serialization (.pkl)
       │
       ▼
Streamlit Dashboard
       │
       ▼
Cloud Deployment
```

---

## Technology Stack

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Database

- SQLite

### Machine Learning

- Scikit-Learn
- XGBoost

### Model Selection & Optimization

- GridSearchCV
- Cross Validation

### Model Explainability

- SHAP

### Visualization

- Matplotlib
- Seaborn

### Model Persistence

- Joblib

### Web Application

- Streamlit

### Version Control

- Git
- GitHub

### Deployment

- Streamlit Community Cloud

---

## Machine Learning Workflow

### 1. Data Collection

Data was retrieved from a SQLite database and loaded into Pandas DataFrames for analysis.

### 2. Data Preprocessing

Performed:

- Missing value handling
- Data cleaning
- Data transformation
- Feature selection

### 3. Feature Engineering

Created predictive features using invoice-related attributes including:

- Quantity
- Invoice Dollar Amount

### 4. Model Training

The following regression algorithms were trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

### 5. Hyperparameter Tuning

GridSearchCV was applied to optimize XGBoost model performance.

Best Parameters:

```python
{
    "learning_rate": 0.05,
    "max_depth": 2,
    "n_estimators": 200
}
```

### 6. Model Explainability

SHAP values were used to understand feature contributions and improve model interpretability.

### 7. Deployment

The final application was deployed using Streamlit Community Cloud.

---

## Model Performance

### Linear Regression (Selected Model)

| Metric | Score |
|----------|----------|
| R² Score | 97.00% |
| MAE | 24.46 |
| RMSE | 124.43 |

### Decision Tree Regressor

| Metric | Score |
|----------|----------|
| R² Score | 96.30% |
| MAE | 38.12 |
| RMSE | 138.25 |

### Random Forest Regressor

| Metric | Score |
|----------|----------|
| R² Score | 96.70% |
| MAE | 30.27 |
| RMSE | 130.63 |

### XGBoost Regressor

| Metric | Score |
|----------|----------|
| R² Score | 95.40% |
| MAE | 26.96 |
| RMSE | 154.20 |

---

## Why Linear Regression Was Selected

Although multiple models were evaluated, Linear Regression achieved:

- Highest R² Score
- Lowest MAE
- Lowest RMSE

Final Performance:

```text
R² Score : 97.00%
MAE      : 24.46
RMSE     : 124.43
```

Therefore, Linear Regression was chosen as the production model for deployment.

---

## Project Structure

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

## Application Features

### Model Performance Dashboard

Displays:

- R² Score
- MAE
- RMSE

### Freight Cost Prediction

Users can enter:

- Quantity
- Invoice Dollar Amount

and instantly receive:

- Predicted Freight Cost

### Business Insights

Provides:

- Cost forecasting support
- Procurement planning assistance
- Freight optimization guidance

---

## Installation

Clone the repository:

```bash
git clone https://github.com/bitwise-arnesh/InvoiceLens.git
```

Navigate to project directory:

```bash
cd InvoiceLens
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Training Pipeline

```bash
python src/main.py
```

---

## Running the Web Application

```bash
streamlit run app.py
```

---

## Live Application

https://invoicelens.streamlit.app

---

## Business Impact

- Improved freight cost forecasting
- Better budgeting decisions
- Vendor freight optimization
- Data-driven procurement planning
- Reduced manual estimation effort
- Faster decision-making process

---

## Key Learning Outcomes

Through this project:

- Built a complete machine learning pipeline
- Worked with relational databases using SQLite
- Compared multiple regression algorithms
- Applied GridSearchCV for hyperparameter tuning
- Used SHAP for model explainability
- Serialized models using Joblib
- Developed interactive applications with Streamlit
- Deployed production-ready ML solutions to the cloud

---

## Author

### Arnesh Bera

Computer Science Engineering Student

Areas of Interest:

- Machine Learning
- Data Science
- Artificial Intelligence
- Generative AI

GitHub:
https://github.com/bitwise-arnesh

LinkedIn:
https://www.linkedin.com/in/arnesh-bera

---
