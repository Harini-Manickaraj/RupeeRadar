import joblib
import numpy as np

# load trained model
model = joblib.load("fragility_model.pkl")

print("\nEnter user financial details\n")

age = int(input("Age: "))
industry = int(input("Industry (encoded number): "))
experience = int(input("Experience level (encoded): "))
income = float(input("Monthly Income: "))
expense = float(input("Monthly Expense: "))
savings = float(input("Savings amount: "))
debt = float(input("Debt amount: "))
dependents = int(input("Number of dependents: "))
work_hours = int(input("Work hours level (encoded): "))
job_stability = int(input("Job stability (1-5): "))
job_satisfaction = int(input("Job satisfaction (1-5): "))
skill_upgrade_time = int(input("Skill upgrade gap (encoded): "))
skill_learning_frequency = int(input("Skill learning frequency (encoded): "))
industry_growth = int(input("Industry growth (encoded): "))
job_security_confidence = int(input("Job security confidence (1-5): "))

# derived features
savings_ratio = savings / (income + 1)
debt_ratio = debt / (income + 1)
expense_ratio = expense / (income + 1)
financial_stress_index = (debt + expense) / (income + 1)
emergency_buffer_months = savings / (expense + 1)

# create feature vector
user_data = np.array([[age, industry, experience, income, expense,
                       savings, debt, dependents, work_hours,
                       job_stability, job_satisfaction,
                       skill_upgrade_time, skill_learning_frequency,
                       industry_growth, job_security_confidence,
                       savings_ratio, debt_ratio, expense_ratio,
                       financial_stress_index, emergency_buffer_months]])

# prediction
risk = model.predict(user_data)[0]

# fragility score formula
fragility_score = (
    0.35 * debt_ratio
    + 0.25 * expense_ratio
    - 0.30 * savings_ratio
    + 0.10 * financial_stress_index
)

fragility_score = round(fragility_score * 100, 2)

print("\n===== RESULT =====")

if risk == 1:
    print("⚠ Financial Risk Detected")
else:
    print("✅ Financially Stable")

print("Fragility Score:", fragility_score, "%")