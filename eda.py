import pandas as pd


# ==========================================
# 1. Dataset path
# ==========================================

DATA_PATH = "data/processed/cicids2017_clean.csv"


# ==========================================
# 2. Load dataset
# ==========================================

df = pd.read_csv(DATA_PATH)


# ==========================================
# 3. Dataset shape
# ==========================================

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(df.shape)


# ==========================================
# 4. First 5 rows
# ==========================================

print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)

print(df.head())


# ==========================================
# 5. Column names
# ==========================================

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(df.columns.tolist())


# ==========================================
# 6. Dataset information
# ==========================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()


# ==========================================
# 7. Label distribution
# ==========================================

print("\n" + "=" * 60)
print("LABEL DISTRIBUTION")
print("=" * 60)

print(
    df["Label"].value_counts()
)


# ==========================================
# 8. Label percentages
# ==========================================

print("\n" + "=" * 60)
print("LABEL PERCENTAGES")
print("=" * 60)

label_percentages = (
    df["Label"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(label_percentages)


# ==========================================
# 9. Missing values
# ==========================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

print(
    missing_values[missing_values > 0]
)