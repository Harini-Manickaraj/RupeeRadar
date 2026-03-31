import streamlit as st

st.title("📝 Financial Fragility Assessment")

# INPUTS
age = st.number_input("Age", 18, 100)

industry = st.selectbox("Industry", ["IT","Education","Government","Manufacturing","Business"])
experience = st.selectbox("Experience", ["Less than 1 year","1-3 years","3-5 years","5-10 years","10+ years"])

income = st.number_input("Monthly Income")
expense = st.number_input("Monthly Expense")
savings = st.number_input("Savings")
debt = st.number_input("Debt")
dependents = st.number_input("Dependents", 0)

work_hours = st.selectbox("Work Hours", ["<30","30-40","40-50","50-60",">60"])

job_stability = st.slider("Job Stability", 1, 5)
job_satisfaction = st.slider("Job Satisfaction", 1, 5)

skill_upgrade = st.selectbox("Skill Upgrade Gap", ["6 months","1 year","1-3 years","3+ years","Never"])
learning_freq = st.selectbox("Learning Frequency", ["Never","Rarely","Occasionally","Frequently","Very Frequently"])
industry_growth = st.selectbox("Industry Growth", ["Declining","Slightly Declining","Stable","Growing","Rapidly Growing"])
job_security = st.slider("Job Security Confidence", 1, 5)

# BUTTON
if st.button("🚀 Analyze Risk"):

    st.session_state["user_data"] = {
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
        "skill_upgrade": skill_upgrade,
        "learning_freq": learning_freq,
        "industry_growth": industry_growth,
        "job_security": job_security
    }

    st.success("Data saved! Go to Dashboard page 👉")