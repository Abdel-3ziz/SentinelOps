import pandas as pd
import joblib
import matplotlib.pyplot as plt


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
# 5. Features to Analyze
# ==========================================

features = [
    "Flow Duration",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Packet Length Mean",
    "Packet Length Std",
    "Average Packet Size",
]


# ==========================================
# 6. Print Group Sizes
# ==========================================

print("=" * 70)
print("DISTRIBUTION ANALYSIS")
print("=" * 70)

print(f"\nXSS correct samples: {len(xss_correct)}")
print(f"XSS -> Brute errors: {len(xss_wrong)}")
print(f"Brute Force correct samples: {len(brute_correct)}")


# ==========================================
# 7. Analyze Each Feature
# ==========================================

for feature in features:

    print("\n" + "=" * 70)
    print(f"FEATURE: {feature}")
    print("=" * 70)

    print("\nMean:")
    print(f"XSS Correct       : {xss_correct[feature].mean():.3f}")
    print(f"XSS -> Brute      : {xss_wrong[feature].mean():.3f}")
    print(f"Brute Correct     : {brute_correct[feature].mean():.3f}")

    print("\nMedian:")
    print(f"XSS Correct       : {xss_correct[feature].median():.3f}")
    print(f"XSS -> Brute      : {xss_wrong[feature].median():.3f}")
    print(f"Brute Correct     : {brute_correct[feature].median():.3f}")


# ==========================================
# 8. Plot Distributions
# ==========================================

for feature in features:

    plt.figure(figsize=(10, 6))

    plt.hist(
        xss_correct[feature],
        bins=50,
        alpha=0.5,
        label="XSS Correct"
    )

    plt.hist(
        xss_wrong[feature],
        bins=50,
        alpha=0.5,
        label="XSS -> Brute"
    )

    plt.hist(
        brute_correct[feature],
        bins=50,
        alpha=0.5,
        label="Brute Correct"
    )

    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.title(f"Distribution: {feature}")
    plt.legend()
    plt.tight_layout()

    plt.show()