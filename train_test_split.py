import pandas as pd

from sklearn.model_selection import train_test_split


# ==========================================
# 1. Dataset path
# ==========================================

DATA_PATH = (
    "data/processed/"
    "cicids2017_features_selected.csv"
)


# ==========================================
# 2. Load selected dataset
# ==========================================

print("=" * 60)
print("TRAIN / TEST SPLIT")
print("=" * 60)

print("\nLoading dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")

print("\nDataset shape:")
print(df.shape)


# ==========================================
# 3. Separate features and target
# ==========================================

X = df.drop(columns=["Label"])

y = df["Label"]


print("\nNumber of features:")
print(X.shape[1])

print("\nNumber of labels:")
print(y.shape[0])


# ==========================================
# 4. Check class distribution
# ==========================================

print("\n" + "=" * 60)
print("CLASS DISTRIBUTION")
print("=" * 60)

print(
    y.value_counts()
)


# ==========================================
# 5. Split dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


# ==========================================
# 6. Display split sizes
# ==========================================

print("\n" + "=" * 60)
print("SPLIT RESULTS")
print("=" * 60)

print("\nTraining features:")
print(X_train.shape)

print("\nTesting features:")
print(X_test.shape)

print("\nTraining labels:")
print(y_train.shape)

print("\nTesting labels:")
print(y_test.shape)


# ==========================================
# 7. Check training class distribution
# ==========================================

print("\n" + "=" * 60)
print("TRAINING CLASS DISTRIBUTION")
print("=" * 60)

print(
    y_train.value_counts()
)


# ==========================================
# 8. Check testing class distribution
# ==========================================

print("\n" + "=" * 60)
print("TESTING CLASS DISTRIBUTION")
print("=" * 60)

print(
    y_test.value_counts()
)


# ==========================================
# 9. Save training and testing data
# ==========================================

print("\n" + "=" * 60)
print("SAVING SPLIT DATA")
print("=" * 60)


train_df = X_train.copy()

train_df["Label"] = y_train


test_df = X_test.copy()

test_df["Label"] = y_test


TRAIN_PATH = (
    "data/processed/"
    "train.csv"
)

TEST_PATH = (
    "data/processed/"
    "test.csv"
)


train_df.to_csv(
    TRAIN_PATH,
    index=False
)


test_df.to_csv(
    TEST_PATH,
    index=False
)


# ==========================================
# 10. Final message
# ==========================================

print("\nTraining data saved to:")
print(TRAIN_PATH)

print("\nTesting data saved to:")
print(TEST_PATH)


print("\n" + "=" * 60)
print("TRAIN / TEST SPLIT COMPLETED")
print("=" * 60)