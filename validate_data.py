import pandas as pd
import numpy as np


# ==========================================
# 1. Dataset path
# ==========================================

DATA_PATH = "data/processed/cicids2017_clean.csv"


# ==========================================
# 2. Load dataset
# ==========================================

df = pd.read_csv(DATA_PATH)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()


# ==========================================
# 3. Basic information
# ==========================================

print("=" * 60)
print("DATA VALIDATION")
print("=" * 60)

print("\nDataset shape:")
print(df.shape)


# ==========================================
# 4. Check Label column
# ==========================================

print("\n" + "=" * 60)
print("LABEL CHECK")
print("=" * 60)

if "Label" in df.columns:
    print("OK: Label column exists.")
else:
    print("ERROR: Label column does not exist.")


# ==========================================
# 5. Check missing values
# ==========================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_total = df.isnull().sum().sum()

print("Total missing values:")
print(missing_total)

if missing_total == 0:
    print("OK: No missing values found.")
else:
    print("WARNING: Missing values found.")


# ==========================================
# 6. Check infinite values
# ==========================================

print("\n" + "=" * 60)
print("INFINITE VALUES")
print("=" * 60)

# Select only numeric columns
numeric_df = df.select_dtypes(include="number")

infinite_total = np.isinf(numeric_df).sum().sum()

print("Total infinite values:")
print(infinite_total)

if infinite_total == 0:
    print("OK: No infinite values found.")
else:
    print("WARNING: Infinite values found.")


# ==========================================
# 7. Check duplicate rows
# ==========================================

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicate_total = df.duplicated().sum()

print("Total duplicate rows:")
print(duplicate_total)

if duplicate_total == 0:
    print("OK: No duplicate rows found.")
else:
    print("WARNING: Duplicate rows found.")


# ==========================================
# 8. Check duplicate column names
# ==========================================

print("\n" + "=" * 60)
print("DUPLICATE COLUMNS")
print("=" * 60)

duplicate_columns = df.columns[
    df.columns.duplicated()
].tolist()

if len(duplicate_columns) == 0:
    print("OK: No duplicate column names.")
else:
    print("WARNING: Duplicate column names:")
    print(duplicate_columns)


# ==========================================
# 9. Check non-numeric features
# ==========================================

print("\n" + "=" * 60)
print("NON-NUMERIC FEATURES")
print("=" * 60)

# Remove target column
X = df.drop(columns=["Label"])

non_numeric_features = X.select_dtypes(
    exclude="number"
).columns.tolist()

if len(non_numeric_features) == 0:
    print("OK: All features are numeric.")
else:
    print("WARNING: Non-numeric features found:")
    
    for column in non_numeric_features:
        print("-", column)


# ==========================================
# 10. Number of classes
# ==========================================

print("\n" + "=" * 60)
print("LABEL INFORMATION")
print("=" * 60)

number_of_classes = df["Label"].nunique()

print("Number of classes:")
print(number_of_classes)

print("\nClass names:")

for label in sorted(df["Label"].astype(str).unique()):
    print("-", label)


# ==========================================
# 11. Constant features
# ==========================================

print("\n" + "=" * 60)
print("CONSTANT FEATURES")
print("=" * 60)

constant_features = []

for column in X.columns:

    if X[column].nunique(dropna=False) <= 1:
        constant_features.append(column)


if len(constant_features) == 0:
    print("OK: No constant features found.")
else:
    print("Constant features:")

    for column in constant_features:
        print("-", column)


# ==========================================
# 12. Final summary
# ==========================================

print("\n" + "=" * 60)
print("VALIDATION SUMMARY")
print("=" * 60)

if (
    "Label" in df.columns
    and missing_total == 0
    and infinite_total == 0
    and len(duplicate_columns) == 0
    and len(non_numeric_features) == 0
):

    print("Dataset passed the basic validation checks.")

else:

    print("Dataset needs additional checking.")