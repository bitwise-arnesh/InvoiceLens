# InvoiceLens – Interview Notes

## 1. Project Overview

### Project Title

InvoiceLens: AI-Powered Vendor Invoice Analytics and Freight Cost Prediction System

### Problem Statement

Organizations receive thousands of vendor invoices containing purchase quantities, invoice amounts, and freight charges. Estimating freight costs manually can be inaccurate and time-consuming.

The goal of this project is to analyze vendor invoice data and build a machine learning model capable of predicting freight costs using historical purchasing patterns.

---

## 2. Business Objective

The project aims to:

* Analyze vendor purchasing behavior
* Understand factors affecting freight cost
* Forecast freight expenses before invoice arrival
* Support budgeting and procurement planning
* Enable data-driven vendor negotiations

---

## 3. Dataset Overview

### Data Source

SQLite Database:

inventory.db

### Main Table Used

vendor_invoice

### Total Records

5,543+ vendor invoices

### Important Features

| Feature      | Description               |
| ------------ | ------------------------- |
| VendorNumber | Vendor Identifier         |
| VendorName   | Vendor Name               |
| InvoiceDate  | Invoice Date              |
| Quantity     | Number of Units Purchased |
| Dollars      | Invoice Amount            |
| Freight      | Freight Cost              |
| Approval     | Approval Status           |

---

## 4. Machine Learning Problem Type

### Category

Supervised Learning

### Task

Regression

### Why Regression?

The target variable (Freight) is a continuous numerical value.

Examples:

Freight = 3.47

Freight = 429.20

Freight = 2935.20

Since the output is numeric rather than categorical, this is a regression problem.

---

## 5. Target Variable

Freight

The model will learn relationships between invoice characteristics and freight cost.

---

## 6. Features Used

Current Features:

* Quantity
* Dollars

Potential Future Features:

* Vendor Information
* Purchase Dates
* Historical Vendor Trends

---

## 7. Exploratory Data Analysis (EDA)

### Activities Performed

* Connected to SQLite database
* Inspected available tables
* Loaded vendor invoice data
* Viewed sample records
* Examined feature relationships

### Purpose

Understand dataset structure before model development.

---

## 8. Correlation Analysis

### Features Evaluated

* Quantity
* Dollars
* Freight

### Results

Quantity ↔ Freight = 0.95

Dollars ↔ Freight = 0.99

### Insight

Both Quantity and Dollars show strong positive relationships with Freight Cost.

As purchase quantity or invoice amount increases, freight cost generally increases.

---

## 9. Data Visualization

### Techniques Used

#### Heatmap

Used to visualize correlation strengths among numerical variables.

#### Scatter Plot

Used to analyze relationships between:

* Quantity vs Freight
* Dollars vs Freight

### Findings

Clear positive trend observed between features and freight cost.

---

## 10. Feature Engineering

### New Feature Created

freight_per_unit

Formula:

Freight / Quantity

### Purpose

Measure shipping cost efficiency.

### Example

Freight = 100

Quantity = 200

Freight Per Unit = 0.50

### Business Value

Provides insight into transportation efficiency across vendors.

---

## 11. Business Insights Identified

### Insight 1

Higher invoice value generally leads to higher freight cost.

### Insight 2

Higher purchase quantities generally lead to higher freight cost.

### Insight 3

Large orders tend to have lower freight cost per unit.

This suggests economies of scale in transportation.

---

## 12. Technologies Used

* Python
* Pandas
* SQLite
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 13. Current ML Pipeline

Completed:

✔ Data Collection

✔ Data Loading

✔ Exploratory Data Analysis

✔ Correlation Analysis

✔ Data Visualization

✔ Feature Engineering

Upcoming:

⬜ Train-Test Split

⬜ Model Training

⬜ Model Evaluation

⬜ Hyperparameter Tuning

⬜ Deployment

---

# Interview Questions & Answers

## Q1. Explain your project in 60 seconds.

This project focuses on vendor invoice analytics and freight cost prediction. I analyzed over 5,500 vendor invoices stored in a SQLite database, performed exploratory data analysis and feature engineering, and identified strong relationships between invoice quantity, invoice value, and freight cost. The goal is to build a regression model that predicts freight expenses in advance, helping organizations improve budgeting and procurement decisions.

---

## Q2. Why is this a machine learning problem?

Freight cost depends on multiple variables such as quantity purchased and invoice amount. Instead of manually defining rules, a machine learning model can learn patterns from historical invoices and predict future freight costs automatically.

---

## Q3. Why is this a regression problem?

The target variable, Freight, is a continuous numerical value. Since the output is numeric rather than categorical, regression is the appropriate machine learning approach.

---

## Q4. What EDA did you perform?

I explored the database structure, inspected the vendor_invoice table, analyzed feature relationships using correlation matrices, and visualized relationships using heatmaps and scatter plots.

---

## Q5. What feature engineering did you perform?

I created a derived feature called freight_per_unit by dividing freight cost by quantity purchased. This helped analyze transportation efficiency and vendor shipping behavior.

---

## Q6. What insights did you discover?

I found strong positive correlations between Quantity, Dollars, and Freight Cost. Additionally, larger orders often showed lower freight cost per unit, indicating economies of scale.

---

## Q7. Why perform correlation analysis?

Correlation analysis helps determine whether features have predictive power. Features with stronger relationships to the target variable are generally better candidates for machine learning models.

---

## Q8. Why create visualizations?

Visualizations validate statistical findings and help identify trends, relationships, and anomalies before training machine learning models.

---

## Q9. What would be your next step?

The next step is preparing the data for modeling by selecting features, performing a train-test split, training regression models, and evaluating their predictive performance.

---

## Q10. How would this help a business?

The solution can estimate freight costs before invoices arrive, improving budgeting accuracy, procurement planning, and vendor cost analysis.
