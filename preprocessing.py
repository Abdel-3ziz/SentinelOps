import os
import pandas as pd
import numpy as np


# ==========================================
# 1. Define folders
# ==========================================

raw_folder = "data/raw"
processed_folder = "data/processed"


# ==========================================
# 2. Create processed folder if not exists
# ==========================================

os.makedirs(processed_folder, exist_ok=True)


# ==========================================
# 3. Get all CSV files from raw folder
# ==========================================

files = [
    file
    for file in os.listdir(raw_folder)
    if file.lower().endswith(".csv")
]


print("=" * 60)
print("SENTINELX PREPROCESSING")
print("=" * 60)

print("\nNumber of CSV files found:")
print(len(files))


print("\nFiles:")

for file in files:
    print("-", file)


# ==========================================
# 4. Create list for cleaned datasets
# ==========================================

all_data = []


# ==========================================
# 5. Process every CSV file
# ==========================================

for file in files:

    print("\n" + "=" * 60)
    print("Processing:", file)
    print("=" * 60)

    # --------------------------------------
    # Build file path
    # --------------------------------------

    file_path = os.path.join(
        raw_folder,
        file
    )


    # --------------------------------------
    # Load dataset
    # --------------------------------------

    try:

        df = pd.read_csv(file_path)

    except Exception as error:

        print("ERROR while reading file:")
        print(error)

        print("Skipping this file.")

        continue


    print("Original shape:")
    print(df.shape)


    # --------------------------------------
    # Clean column names
    # --------------------------------------

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )


    # --------------------------------------
    # Check Label column
    # --------------------------------------

    if "Label" not in df.columns:

        print("WARNING: Label column not found.")
        print("Skipping this file.")

        continue


    # --------------------------------------
    # Remove infinity values
    # --------------------------------------

    df = df.replace(
        [np.inf, -np.inf],
        np.nan
    )


    # --------------------------------------
    # Remove missing values
    # --------------------------------------

    missing_before = df.isnull().sum().sum()

    df = df.dropna()

    missing_removed = missing_before


    # --------------------------------------
    # Remove duplicate rows
    # inside current file
    # --------------------------------------

    duplicates_before = len(df)

    df = df.drop_duplicates()

    duplicates_removed = (
        duplicates_before - len(df)
    )


    # --------------------------------------
    # Print cleaned information
    # --------------------------------------

    print("\nCleaning results:")

    print(
        "Missing values removed:",
        missing_removed
    )

    print(
        "Duplicates removed inside file:",
        duplicates_removed
    )

    print(
        "Cleaned shape:",
        df.shape
    )


    # --------------------------------------
    # Add cleaned dataset to list
    # --------------------------------------

    all_data.append(df)


# ==========================================
# 6. Check if datasets were loaded
# ==========================================

if len(all_data) == 0:

    raise ValueError(
        "No valid datasets were found."
    )


# ==========================================
# 7. Combine all datasets
# ==========================================

print("\n" + "=" * 60)
print("COMBINING ALL DATASETS")
print("=" * 60)


combined_df = pd.concat(
    all_data,
    ignore_index=True
)


print("\nShape before final duplicate removal:")

print(
    combined_df.shape
)


# ==========================================
# 8. Remove duplicates AFTER combining
# ==========================================

print("\n" + "=" * 60)
print("FINAL DUPLICATE REMOVAL")
print("=" * 60)


duplicates_before = len(combined_df)


combined_df = combined_df.drop_duplicates(
    ignore_index=True
)


duplicates_removed_after_combine = (
    duplicates_before - len(combined_df)
)


print(
    "Duplicates removed after combining:",
    duplicates_removed_after_combine
)


print(
    "Shape after duplicate removal:"
)

print(
    combined_df.shape
)


# ==========================================
# 9. Clean Label values
# ==========================================

combined_df["Label"] = (
    combined_df["Label"]
    .astype(str)
    .str.strip()
)


# ==========================================
# 10. Final missing value check
# ==========================================

print("\n" + "=" * 60)
print("FINAL DATA QUALITY CHECK")
print("=" * 60)


final_missing = (
    combined_df
    .isnull()
    .sum()
    .sum()
)


print(
    "Final missing values:",
    final_missing
)


# ==========================================
# 11. Final infinite value check
# ==========================================

numeric_columns = combined_df.select_dtypes(
    include="number"
)


final_infinite = np.isinf(
    numeric_columns
).sum().sum()


print(
    "Final infinite values:",
    final_infinite
)


# ==========================================
# 12. Final duplicate check
# ==========================================

final_duplicates = (
    combined_df
    .duplicated()
    .sum()
)


print(
    "Final duplicate rows:",
    final_duplicates
)


# ==========================================
# 13. Final dataset shape
# ==========================================

print("\n" + "=" * 60)
print("FINAL DATASET")
print("=" * 60)


print("\nFinal dataset shape:")

print(
    combined_df.shape
)


# ==========================================
# 14. Final label distribution
# ==========================================

print("\nFinal label distribution:")

print(
    combined_df["Label"]
    .value_counts()
)


# ==========================================
# 15. Number of classes
# ==========================================

print("\nNumber of classes:")

print(
    combined_df["Label"].nunique()
)


# ==========================================
# 16. Class names
# ==========================================

print("\nClass names:")

for label in sorted(
    combined_df["Label"].unique()
):

    print(
        "-",
        label
    )


# ==========================================
# 17. Save final cleaned dataset
# ==========================================

output_path = os.path.join(
    processed_folder,
    "cicids2017_clean.csv"
)


combined_df.to_csv(
    output_path,
    index=False
)


# ==========================================
# 18. Final success message
# ==========================================

print("\n" + "=" * 60)
print("PREPROCESSING COMPLETED")
print("=" * 60)


print(
    "\nFinal cleaned dataset saved to:"
)

print(
    output_path
)


print(
    "\nFinal number of rows:",
    len(combined_df)
)


print(
    "Final number of columns:",
    len(combined_df.columns)
)


print(
    "Final duplicate rows:",
    final_duplicates
)