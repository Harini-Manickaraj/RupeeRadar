import streamlit as st
import pandas as pd
import joblib
from recommendation_engine import generate_recommendations

st.title("📊 Risk Assessment Dashboard")

if "user_data" not in st.session_state:
    st.warning("Please enter data in Input page first.")
    st.stop()

data = st.session_state["user_data"]

model = joblib.load("fragility_model.pkl")

# ---------------- ENCODING ----------------
industry_map = {"IT":1,"Education":2,"Government":3,"Manufacturing":4,"Business":5}
exp_map = {"Less than 1 year":1,"1-3 years":2,"3-5 years":3,"5-10 years":4,"10+ years":5}
work_map = {"<30":1,"30-40":2,"40-50":3,"50-60":4,">60":5}
skill_map = {"6 months":1,"1 year":2,"1-3 years":3,"3+ years":4,"Never":5}
learn_map = {"Never":1,"Rarely":2,"Occasionally":3,"Frequently":4,"Very Frequently":5}
growth_map = {"Declining":1,"Slightly Declining":2,"Stable":3,"Growing":4,"Rapidly Growing":5}

# ---------------- RATIOS ----------------
income = data["income"]
expense = data["expense"]
savings = data["savings"]
debt = data["debt"]

savings_ratio = savings / (income + 1)
debt_ratio = debt / (income + 1)
expense_ratio = expense / (income + 1)
stress = (debt + expense) / (income + 1)
buffer = savings / (expense + 1)

# ---------------- MODEL ----------------
user_df = pd.DataFrame([{
    "age": data["age"],
    "industry": industry_map[data["industry"]],
    "experience": exp_map[data["experience"]],
    "income": income,
    "expense": expense,
    "savings": savings,
    "debt": debt,
    "dependents": data["dependents"],
    "work_hours": work_map[data["work_hours"]],
    "job_stability": data["job_stability"],
    "job_satisfaction": data["job_satisfaction"],
    "skill_upgrade_time": skill_map[data["skill_upgrade"]],
    "skill_learning_frequency": learn_map[data["learning_freq"]],
    "industry_growth": growth_map[data["industry_growth"]],
    "job_security_confidence": data["job_security"],
    "savings_ratio": savings_ratio,
    "debt_ratio": debt_ratio,
    "expense_ratio": expense_ratio,
    "financial_stress_index": stress,
    "emergency_buffer_months": buffer
}])

model.predict(user_df)

# ---------------- SCORE ----------------
score = (
    0.35 * debt_ratio +
    0.25 * expense_ratio -
    0.30 * savings_ratio +
    0.10 * stress
)

score = (score + 1) * 50
score = max(0, min(100, score))
score = round(score, 2)

# ---------------- CATEGORY ----------------
if score <= 20:
    category = "🟢 Very Stable"
elif score <= 40:
    category = "🟢 Stable"
elif score <= 60:
    category = "🟡 Slightly Risky"
elif score <= 80:
    category = "🟠 Moderately Risky"
else:
    category = "🔴 High Risk"

# ---------------- UI ----------------
col1, col2 = st.columns(2)

with col1:
    st.metric("Fragility Score", f"{score}%")

with col2:
    st.success(category)

# ---------------- INSIGHTS ----------------
st.subheader("📊 Financial Insights")

chart_data = pd.DataFrame({
    "Category": ["Savings","Debt","Expense"],
    "Value": [savings, debt, expense]
})

st.bar_chart(chart_data.set_index("Category"))

# ---------------- RECOMMENDATIONS ----------------
st.subheader("💡 Recommendations")

recs = generate_recommendations(
    savings_ratio,
    debt_ratio,
    buffer,
    skill_map[data["skill_upgrade"]],
    work_map[data["work_hours"]]
)

for r in recs:
    st.write("•", r)

# ---------------- FUTURE ----------------
st.subheader("🚀 Future Features")

st.info("""
🤖 AI Chat Assistant  
📈 Risk Trend Over Time  
📊 User History Dashboard  
🔔 Alerts & Notifications  
""")