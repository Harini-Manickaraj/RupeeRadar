import pandas as pd
from sklearn.preprocessing import LabelEncoder

# =============================
# 1️⃣ Load dataset
# =============================
data = pd.read_csv("financial_data.csv", engine="python", on_bad_lines="skip")

# =============================
# 2️⃣ Remove Timestamp column
# =============================
if "Timestamp" in data.columns:
    data = data.drop(columns=["Timestamp"])

# =============================
# 3️⃣ Rename columns properly
# =============================
data.columns = [
    "age",
    "industry",
    "experience",
    "income",
    "expense",
    "savings",
    "debt",
    "dependents",
    "work_hours",
    "job_stability",
    "job_satisfaction",
    "skill_upgrade_time",
    "skill_learning_frequency",
    "industry_growth",
    "job_security_confidence",
    "financial_stability"
]

# =============================
# 4️⃣ Remove invalid age rows
# =============================
data = data[pd.to_numeric(data["age"], errors="coerce").notnull()]
data["age"] = data["age"].astype(int)

# =============================
# 5️⃣ Function to clean money values
# =============================
def clean_money(x):
    x = str(x).lower().replace(",", "").strip()

    if x in ["nil", "no", "none", "_", "-", "", "na"]:
        return 0

    if "k" in x:
        try:
            return float(x.replace("k","")) * 1000
        except:
            return 0

    if "l" in x:
        try:
            return float(x.replace("l","")) * 100000
        except:
            return 0

    try:
        return float(x)
    except:
        return 0

# =============================
# 6️⃣ Clean numeric financial columns
# =============================
for col in ["income", "expense", "savings", "debt"]:
    data[col] = data[col].apply(clean_money)

# =============================
# 7️⃣ Fill missing values
# =============================
data = data.fillna(0)

# =============================
# 8️⃣ Feature Engineering (VERY IMPORTANT)
# =============================
data["savings_ratio"] = data["savings"] / (data["income"] + 1)
data["debt_ratio"] = data["debt"] / (data["income"] + 1)
data["expense_ratio"] = data["expense"] / (data["income"] + 1)

data["financial_stress_index"] = (data["debt"] + data["expense"]) / (data["income"] + 1)

data["emergency_buffer_months"] = data["savings"] / (data["expense"] + 1)

# =============================
# 9️⃣ Convert financial stability → binary risk
# =============================
def convert_risk(x):
    x = str(x).lower()

    if "secure" in x:
        return 0
    elif "stress" in x or "risk" in x:
        return 1
    else:
        return 1

data["financial_risk"] = data["financial_stability"].apply(convert_risk)

# drop old column
data = data.drop(columns=["financial_stability"])

# =============================
# 🔟 Encode categorical columns
# =============================
le = LabelEncoder()

for col in data.columns:
    if data[col].dtype == "object":
        data[col] = le.fit_transform(data[col].astype(str))

# =============================
# 11️⃣ Save cleaned dataset
# =============================
data.to_csv("data.csv", index=False)

print("✅ Data preprocessing completed")
print("✅ Intelligent dataset saved as data.csv")
print("Final Shape:", data.shape)