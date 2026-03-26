import pandas as pd
import joblib

# ======================
# Load trained model
# ======================
model = joblib.load("fragility_model.pkl")

# ======================
# Load dataset to get feature names
# ======================
data = pd.read_csv("data.csv")

X = data.drop("financial_risk", axis=1)

# ======================
# Extract importance
# ======================
importance = model.feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

# sort descending
importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\n===== FEATURE IMPORTANCE =====\n")
print(importance_df)