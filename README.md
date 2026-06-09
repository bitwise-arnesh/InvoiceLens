# 📦 InvoiceLens: End-to-End Freight Cost Prediction System

<div align="center">

## Machine Learning-Based Freight Cost Forecasting for Vendor Invoices

Predict freight costs from invoice data using Machine Learning, enabling better procurement planning, budgeting, and logistics decision-making.

### 🚀 Live Demo

https://invoicelens.streamlit.app

### 📊 Model Performance

| Metric   | Score      |
| -------- | ---------- |
| R² Score | **97.06%** |
| MAE      | **24.46**  |
| RMSE     | **124.43** |

</div>

---

# 1. Overview

InvoiceLens is an end-to-end Machine Learning application that predicts vendor freight costs using historical invoice information.

The project demonstrates the complete ML lifecycle:

1. Data Storage
2. Data Extraction
3. Data Cleaning
4. Exploratory Data Analysis
5. Feature Engineering
6. Model Training
7. Model Evaluation
8. Model Selection
9. Model Serialization
10. Streamlit Application Development
11. Cloud Deployment

The system helps procurement teams estimate freight expenses before invoice processing, improving cost visibility and financial planning.

---

# 2. Business Problem

Freight costs significantly impact procurement and logistics budgets.

Manual estimation often results in:

* Budget overruns
* Inaccurate forecasting
* Poor vendor cost planning
* Limited visibility into shipping expenses

InvoiceLens addresses this challenge by automatically estimating freight costs from invoice characteristics.

---

# 3. Dataset & Features

The model was trained using vendor invoice transaction records.

## Input Features

| Feature  | Description               |
| -------- | ------------------------- |
| Quantity | Number of units purchased |
| Dollars  | Invoice amount in USD     |

## Target Variable

| Variable     | Description              |
| ------------ | ------------------------ |
| Freight Cost | Shipping/Freight expense |

---

# 4. Project Workflow

## Step 1: Data Storage

Invoice records were stored and managed using:

```text
SQLite
```

This allowed structured querying and efficient retrieval of invoice transactions.

---

## Step 2: Data Extraction

Invoice records were loaded from SQLite into Pandas DataFrames for analysis and preprocessing.

Technologies:

```text
SQLite
Pandas
```

---

## Step 3: Data Preprocessing

Performed:

* Data validation
* Feature selection
* Data cleaning
* Train-test split

Libraries:

```python
pandas
numpy
```

---

## Step 4: Exploratory Data Analysis

Conducted EDA to understand:

* Freight cost distribution
* Quantity patterns
* Invoice value trends
* Feature relationships
* Outlier behavior

Libraries:

```python
matplotlib
seaborn
```

---

## Step 5: Model Training

Three regression models were trained and compared.

### Model 1

```python
LinearRegression()
```

### Model 2

```python
RandomForestRegressor()
```

### Model 3

```python
XGBRegressor()
```

---

## Step 6: Model Evaluation

Models were evaluated using:

### R² Score

Measures variance explained by the model.

### MAE (Mean Absolute Error)

Measures average prediction error.

### RMSE (Root Mean Squared Error)

Measures prediction deviation.

---

## Step 7: Model Selection

After comparing multiple regression models, the best-performing model was selected for deployment.

Selected model:

```python
Linear Regression
```

Advantages:

* High accuracy
* Fast inference
* Lightweight deployment
* Easy interpretability

---

## Step 8: Model Serialization

The trained model was saved using:

```python
joblib
```

Output:

```text
linear_regression.pkl
```

---

## Step 9: Streamlit Deployment

Built an interactive Streamlit application for real-time freight cost prediction.

Features include:

✅ Real-time predictions

✅ Interactive dashboard

✅ Business KPI display

✅ Responsive UI

✅ Cloud deployment

---

# 5. Final Model Performance

| Metric   | Value  |
| -------- | ------ |
| R² Score | 97.06% |
| MAE      | 24.46  |
| RMSE     | 124.43 |

---

# 6. Application Screenshots

## Dashboard

<img width="100%" alt="Dashboard Screenshot" src="assets/dashboard.png">

## Prediction Output

<img width="100%" alt="Prediction Screenshot" src="assets/prediction.png">

---

# 7. System Architecture

```text
                ┌─────────────────┐
                │ SQLite Database │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Data Extraction │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Preprocessing   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Feature Creation│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Training  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Selection │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Saved Model     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Streamlit App   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Cloud Deployment│
                └─────────────────┘
```

---

# 8. Tech Stack

## Programming Language

* Python

## Database

* SQLite

## Data Processing

* Pandas
* NumPy

## Data Visualization

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-Learn
* XGBoost

## Model Persistence

* Joblib

## Explainability & Analysis

* SHAP

## Web Application

* Streamlit

## Version Control

* Git
* GitHub

## Deployment

* Streamlit Community Cloud

---

# 9. Project Structure

```text
InvoiceLens/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│
├── db/
│   └── invoices.db
│
├── notebooks/
│
├── models/
│   ├── linear_regression.pkl
│   └── tuned_xgboost.pkl
│
├── src/
│
└── assets/
```

---

# 10. Installation

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

Run application:

```bash
streamlit run app.py
```

---

# 11. Live Demo

### Streamlit Application

https://invoicelens.streamlit.app

---

# 12. Key Learning Outcomes

Through this project, I gained experience in:

* End-to-End Machine Learning Pipelines
* Regression Modeling
* Model Evaluation Techniques
* Feature Engineering
* SQLite Database Integration
* Streamlit Development
* Cloud Deployment
* Git & GitHub Workflows
* Production-Oriented ML Systems

---

# 13. Resume Highlights

* Built an end-to-end freight cost prediction system using Machine Learning and SQLite.
* Trained and evaluated multiple regression models including Linear Regression, Random Forest, and XGBoost.
* Achieved **97.06% R² Score** on freight cost forecasting.
* Developed and deployed a Streamlit application for real-time prediction.
* Implemented the complete ML workflow from database extraction to cloud deployment.

---

# 14. Author

### Arnesh Bera

Computer Science Engineering Student

GitHub: https://github.com/bitwise-arnesh

LinkedIn: https://www.linkedin.com/in/arnesh-bera

---

⭐ If you found this project useful, consider starring the repository.
