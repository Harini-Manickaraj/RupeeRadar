import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# =========================
# 1️⃣ LOAD PROCESSED DATA
# =========================
data = pd.read_csv("data.csv")

print("Dataset Shape:", data.shape)

# =========================
# 2️⃣ DEFINE FEATURES & TARGET
# =========================
X = data.drop("financial_risk", axis=1)
y = data["financial_risk"]

# =========================
# 3️⃣ DEFINE MODELS
# =========================
models = {
    "Logistic Regression": LogisticRegression(max_iter=2000),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        max_depth=7,
        random_state=42
    )
}

# =========================
# 4️⃣ CROSS VALIDATION
# =========================
print("\n===== MODEL COMPARISON USING 5-FOLD CROSS VALIDATION =====")

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")

    print("\nModel:", name)
    print("Accuracy scores:", scores)
    print("Average Accuracy:", scores.mean())