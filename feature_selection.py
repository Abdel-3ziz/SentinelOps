import pandas as pd


# ==========================================
# 1. Load cleaned dataset
# ==========================================

DATA_PATH = "data/processed/cicids2017_clean.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("FEATURE SELECTION")
print("=" * 60)


# ==========================================
# 2. Separate features and Label
# ==========================================

X = df.drop(columns=["Label"])
y = df["Label"]


print("\nOriginal number of features:")
print(X.shape[1])


# ==========================================
# 3. Find constant features
# ==========================================

constant_features = []

for column in X.columns:

    if X[column].nunique(dropna=False) <= 1:

        constant_features.append(column)


# ==========================================
# 4. Display constant features
# ==========================================

print("\nConstant features found:")
print(len(constant_features))

for feature in constant_features:
    print("-", feature)


# ==========================================
# 5. Remove constant features
# ==========================================

X = X.drop(
    columns=constant_features
)


# ==========================================
# 6. Recombine features with Label
# ==========================================

selected_df = X.copy()

selected_df["Label"] = y


# ==========================================
# 7. Display final number of features
# ==========================================

print("\nNumber of features after removal:")
print(X.shape[1])


# ==========================================
# 8. Save selected dataset
# ==========================================

OUTPUT_PATH = (
    "data/processed/"
    "cicids2017_features_selected.csv"
)

selected_df.to_csv(
    OUTPUT_PATH,
    index=False
)


# ==========================================
# 9. Final message
# ==========================================

print("\n" + "=" * 60)
print("FEATURE SELECTION COMPLETED")
print("=" * 60)

print("\nSaved file:")
print(OUTPUT_PATH)