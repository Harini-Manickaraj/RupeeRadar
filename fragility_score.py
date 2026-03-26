import pandas as pd

data = pd.read_csv("data.csv")

data["fragility_score"] = (
    0.35 * data["debt_ratio"]
    + 0.25 * data["expense_ratio"]
    - 0.30 * data["savings_ratio"]
    + 0.10 * data["financial_stress_index"]
)

# normalize to 0–100
min_val = data["fragility_score"].min()
max_val = data["fragility_score"].max()

data["fragility_score"] = (
    (data["fragility_score"] - min_val) / (max_val - min_val)
) * 100

# round for readability
data["fragility_score"] = data["fragility_score"].round(2)

print((data["fragility_score"] * 100).round(2).head())
# =============================
# Risk Category
# =============================

if fragility_score <= 20:
    risk_level = "🟢 Very Stable"
elif fragility_score <= 40:
    risk_level = "🟢 Stable"
elif fragility_score <= 60:
    risk_level = "🟡 Slightly Risky"
elif fragility_score <= 80:
    risk_level = "🟠 Moderately Risky"
else:
    risk_level = "🔴 High Risk"