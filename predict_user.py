from recommendation_engine import generate_recommendations
import joblib
import numpy as np

# load trained model
model = joblib.load("fragility_model.pkl")

print("\nEnter user financial details\n")

age = int(input("Age: "))

print("\nSelect Industry:")
print("1 IT")
print("2 Education")
print("3 Government")
print("4 Manufacturing")
print("5 Business / Self Employed")
industry = int(input("Enter option number: "))

print("\nExperience Level:")
print("1 Less than 1 year")
print("2 1 – 3 years")
print("3 3 – 5 years")
print("4 5 – 10 years")
print("5 More than 10 years")
experience = int(input("Enter option number: "))

income = float(input("Monthly Income: "))
expense = float(input("Monthly Expense: "))
savings = float(input("Savings amount: "))
debt = float(input("Debt amount: "))
dependents = int(input("Number of dependents: "))

print("\nWork Hours per Week:")
print("1 Less than 30")
print("2 30 – 40")
print("3 40 – 50")
print("4 50 – 60")
print("5 More than 60")
work_hours = int(input("Enter option number: "))

job_stability = int(input("Job Stability (1 low – 5 high): "))
job_satisfaction = int(input("Job Satisfaction (1 low – 5 high): "))

print("\nSkill Upgrade Gap:")
print("1 Within last 6 months")
print("2 Within last 1 year")
print("3 1–3 years ago")
print("4 More than 3 years")
print("5 Never")
skill_upgrade_time = int(input("Enter option number: "))

print("\nSkill Learning Frequency:")
print("1 Never")
print("2 Rarely")
print("3 Occasionally")
print("4 Frequently")
print("5 Very Frequently")
skill_learning_frequency = int(input("Enter option number: "))

print("\nIndustry Growth Trend:")
print("1 Rapidly Declining")
print("2 Slightly Declining")
print("3 Stable")
print("4 Growing")
print("5 Rapidly Growing")
industry_growth = int(input("Enter option number: "))

job_security_confidence = int(input("Job Security Confidence (1 low – 5 high): "))

# derived features
savings_ratio = savings / (income + 1)
debt_ratio = debt / (income + 1)
expense_ratio = expense / (income + 1)
financial_stress_index = (debt + expense) / (income + 1)
emergency_buffer_months = savings / (expense + 1)

# create feature vector
import pandas as pd

user_data = pd.DataFrame([{
    "age": age,
    "industry": industry,
    "experience": experience,
    "income": income,
    "expense": expense,
    "savings": savings,
    "debt": debt,
    "dependents": dependents,
    "work_hours": work_hours,
    "job_stability": job_stability,
    "job_satisfaction": job_satisfaction,
    "skill_upgrade_time": skill_upgrade_time,
    "skill_learning_frequency": skill_learning_frequency,
    "industry_growth": industry_growth,
    "job_security_confidence": job_security_confidence,
    "savings_ratio": savings_ratio,
    "debt_ratio": debt_ratio,
    "expense_ratio": expense_ratio,
    "financial_stress_index": financial_stress_index,
    "emergency_buffer_months": emergency_buffer_months
}])
# prediction
risk = model.predict(user_data)[0]

# fragility score formula
fragility_score = (
    0.35 * debt_ratio
    + 0.25 * expense_ratio
    - 0.30 * savings_ratio
    + 0.10 * financial_stress_index
)

fragility_score = fragility_score * 100

if fragility_score < 0:
    fragility_score = 0
if fragility_score > 100:
    fragility_score = 100

fragility_score = round(fragility_score, 2)

print("\n===== RESULT =====")

if risk == 1:
    print("⚠ Financial Risk Detected")
else:
    print("✅ Financially Stable")

print("Fragility Score:", fragility_score, "%")

# =============================
# Generate Recommendations
# =============================

recommendations = generate_recommendations(
    savings_ratio,
    debt_ratio,
    emergency_buffer_months,
    skill_upgrade_time,
    work_hours
)

print("\n===== RECOMMENDATIONS =====")

for rec in recommendations:
    print("-", rec)

