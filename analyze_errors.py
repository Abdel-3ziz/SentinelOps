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
# 5. Calculate Feature Means
# ==========================================

comparison = pd.DataFrame({
    "XSS_Correct": xss_correct.mean(),
    "XSS_Wrong_As_Brute": xss_wrong.mean(),
    "Brute_Correct": brute_correct.mean()
})


# ==========================================
# 6. Calculate Difference
# ==========================================

comparison["XSS_Error_vs_XSS_Correct"] = (
    comparison["XSS_Wrong_As_Brute"] -
    comparison["XSS_Correct"]
).abs()

comparison["XSS_Error_vs_Brute"] = (
    comparison["XSS_Wrong_As_Brute"] -
    comparison["Brute_Correct"]
).abs()


# ==========================================
# 7. Find Most Interesting Features
# ==========================================

comparison = comparison.sort_values(
    "XSS_Error_vs_Brute"
)


# ==========================================
# 8. Display
# ==========================================

print("=" * 70)
print("XSS vs BRUTE FORCE FEATURE COMPARISON")
print("=" * 70)

print(f"\nXSS correct samples: {len(xss_correct)}")
print(f"XSS -> Brute errors: {len(xss_wrong)}")
print(f"Brute Force correct samples: {len(brute_correct)}")

print("\nFeature comparison:")

print(
    comparison.head(20).round(3).to_string()
)




