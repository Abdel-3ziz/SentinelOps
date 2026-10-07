import pandas as pd
import joblib


# ==========================================
# 1. Load Test Data
# ==========================================

test_df = pd.read_csv("data/processed/test.csv")

X_test = test_df.drop(columns=["Label"])
y_test = test_df["Label"]


# ==========================================
# 2. Load Model
# ==========================================

model = joblib.load("models/random_forest.pkl")

y_pred = model.predict(X_test)


# ==========================================
# 3. Define Labels
# ==========================================

xss = "Web Attack � XSS"
brute = "Web Attack � Brute Force"


# ==========================================
# 4. Create Groups
# ==========================================

xss_correct = X_test[
    (y_test == xss) &
    (y_pred == xss)
]

xss_wrong = X_test[
    (y_test == xss) &
    (y_pred == brute)
]

brute_correct = X_test[
    (y_test == brute) &
    (y_pred == brute)
]


# ==========================================
# 5. Get Feature Importance
# ==========================================

importance = pd.DataFrame({
    "Feature": X_test.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)


# ==========================================
# 6. Select Top 20 Features
# ==========================================

top_features = importance.head(20)["Feature"]


# ==========================================
# 7. Compare Top Features
# ==========================================

comparison = pd.DataFrame({
    "Importance": importance.set_index("Feature").loc[top_features, "Importance"],
    "XSS_Correct_Mean": xss_correct[top_features].mean(),
    "XSS_Wrong_Mean": xss_wrong[top_features].mean(),
    "Brute_Correct_Mean": brute_correct[top_features].mean(),
})


# ==========================================
# 8. Calculate Differences
# ==========================================

comparison["Wrong_vs_XSS"] = (
    comparison["XSS_Wrong_Mean"] -
    comparison["XSS_Correct_Mean"]
).abs()

comparison["Wrong_vs_Brute"] = (
    comparison["XSS_Wrong_Mean"] -
    comparison["Brute_Correct_Mean"]
).abs()


# ==========================================
# 9. Sort by Importance
# ==========================================

comparison = comparison.sort_values(
    "Importance",
    ascending=False
)


# ==========================================
# 10. Display
# ==========================================

print("=" * 90)
print("TOP FEATURES - XSS ERROR ANALYSIS")
print("=" * 90)

print(f"\nXSS correct samples : {len(xss_correct)}")
print(f"XSS -> Brute errors : {len(xss_wrong)}")
print(f"Brute correct       : {len(brute_correct)}")

print("\nTop 20 Feature Comparison:\n")

print(
    comparison.round(4).to_string()
)