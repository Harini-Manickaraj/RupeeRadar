# 💰 RupeeRadar — AI-Driven Economic Fragility Prediction System

## 📌 Project Overview
RupeeRadar is a machine learning–based decision support system designed to predict an individual's potential economic fragility using behavioural, financial, and career-related indicators.  
The system evaluates personal financial patterns and generates both categorical risk predictions and a quantitative fragility severity score to support proactive financial planning.

---

## 🎯 Problem Statement
Traditional financial risk models focus mainly on credit default prediction or loan eligibility assessment.  
However, they fail to detect early signs of **personal economic instability** caused by factors such as:

- Increasing debt burden  
- Declining savings buffer  
- Job instability  
- Skill obsolescence  
- Adverse industry growth trends  

This project aims to address this gap by developing an **AI-driven early warning system** that predicts personal economic fragility risk before severe financial distress occurs.

---

## 🧠 Machine Learning Approach

### ✔ Feature Engineering
Behavioural financial indicators were derived to improve predictive intelligence:

- Savings Ratio  
- Debt-Income Ratio  
- Expense Pressure Index  
- Financial Stress Index  
- Emergency Survival Buffer (months)

### ✔ Classification Model
Binary classification models were evaluated using **5-fold cross-validation**:

- Logistic Regression  
- Decision Tree  
- Random Forest  

The selected model predicts whether an individual is:
- Financially Stable  
- Financially At Risk  

### ✔ Fragility Severity Score
A hybrid statistical risk index was designed to quantify severity:

\[
Fragility\ Score = f(debt\ ratio, expense\ ratio, savings\ ratio, financial\ stress)
\]

This provides a **continuous risk measurement (0–100 scale)**.

### ✔ Explainable AI
Feature importance analysis was performed to identify dominant predictors influencing economic fragility.

---

## 📊 Dataset Description
The dataset was **primary survey data collected using structured questionnaires**, including variables such as:

- Age  
- Industry sector  
- Years of experience  
- Monthly income & expenses  
- Savings & debt level  
- Job stability & satisfaction  
- Skill upgrade frequency  
- Industry growth perception  

This ensures a **behaviour-driven risk modelling framework** rather than relying solely on financial history.

---

## ⚙️ System Pipeline

1. Data Collection via Survey  
2. Data Cleaning & Encoding  
3. Behavioural Feature Engineering  
4. Model Selection using Cross-Validation  
5. Final Model Training  
6. Risk Prediction for New Users  
7. Fragility Score Computation  
8. Risk Factor Interpretation  

---

## 🚀 How to Run the Project

### Install dependencies
```bash
pip install -r requirements.txt