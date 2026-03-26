import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier

# =========================
# LOAD FINAL DATASET
# =========================
data = pd.read_csv("data.csv")

X = data.drop("financial_risk", axis=1)
y = data["financial_risk"]

print("Training on full dataset:", X.shape)

# =========================
# TRAIN FINAL MODEL
# =========================
model = DecisionTreeClassifier(
    max_depth=6,
    random_state=42
)

model.fit(X, y)

print("✅ Final model trained on full dataset")

# =========================
# SAVE MODEL
# =========================
joblib.dump(model, "fragility_model.pkl")

print("✅ Final production model saved as fragility_model.pkl")

import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier

# =========================
# LOAD FINAL DATASET
# =========================
data = pd.read_csv("data.csv")

X = data.drop("financial_risk", axis=1)
y = data["financial_risk"]

print("Training on full dataset:", X.shape)

# =========================
# TRAIN FINAL MODEL
# =========================
model = DecisionTreeClassifier(
    max_depth=6,
    random_state=42
)

model.fit(X, y)

print("✅ Final model trained on full dataset")

# =========================
# SAVE MODEL
# =========================
joblib.dump(model, "fragility_model.pkl")

print("✅ Final production model saved as fragility_model.pkl")