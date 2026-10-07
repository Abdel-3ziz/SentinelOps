import pandas as pd
import joblib
from imblearn.ensemble import BalancedRandomForestClassifier

# ==========================================
# 1. Load training data
# ==========================================

train_df = pd.read_csv("data/processed/train.csv")

X_train = train_df.drop(columns=["Label"])
y_train = train_df["Label"]

print("Training data shape:", X_train.shape)
print("Number of classes:", y_train.nunique())


# ==========================================
# 2. Create Balanced Random Forest
# ==========================================

model = BalancedRandomForestClassifier(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)


# ==========================================
# 3. Train
# ==========================================

print("\nTraining Balanced Random Forest...")

model.fit(X_train, y_train)

print("Training completed.")


# ==========================================
# 4. Save model
# ==========================================

joblib.dump(model, "models/balanced_random_forest.pkl")

print("\nModel saved to:")
print("models/balanced_random_forest.pkl")