import pandas as pd
import joblib


# ==========================================
# 1. Load Model
# ==========================================

model = joblib.load("models/random_forest.pkl")


# ==========================================
# 2. Load Test Data
# ==========================================

test_df = pd.read_csv("data/processed/test.csv")

X_test = test_df.drop(columns=["Label"])


# ==========================================
# 3. Get Feature Importance
# ==========================================

importance = pd.DataFrame({
    "Feature": X_test.columns,
    "Importance": model.feature_importances_
})


# ==========================================
# 4. Sort
# ==========================================

importance = importance.sort_values(
    "Importance",
    ascending=False
)


# ==========================================
# 5. Display
# ==========================================

print("=" * 70)
print("RANDOM FOREST FEATURE IMPORTANCE")
print("=" * 70)

print("\nTop 20 Features:\n")

print(
    importance.head(20).round(6).to_string(index=False)
)