import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import time


# ==========================================
# 1. Load Training Data
# ==========================================

train_path = "data/processed/train.csv"

print("=" * 60)
print("RANDOM FOREST TRAINING")
print("=" * 60)

print("\nLoading training data...")

train_df = pd.read_csv(train_path)

print(f"Training data shape: {train_df.shape}")


# ==========================================
# 2. Separate Features and Label
# ==========================================

X_train = train_df.drop(columns=["Label"])
y_train = train_df["Label"]

print(f"\nX_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")


# ==========================================
# 3. Create Random Forest Model
# ==========================================

print("\nCreating Random Forest model...")

model = RandomForestClassifier(
    n_estimators=50,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)


# ==========================================
# 4. Train Model
# ==========================================

print("\nStarting training...")

start_time = time.time()

model.fit(X_train, y_train)

end_time = time.time()

training_time = end_time - start_time

print("\nTraining completed!")
print(f"Training time: {training_time:.2f} seconds")


# ==========================================
# 5. Save Model
# ==========================================

os.makedirs("models", exist_ok=True)

model_path = "models/random_forest.pkl"

joblib.dump(model, model_path)

print(f"\nModel saved successfully: {model_path}")

print("\n" + "=" * 60)
print("TRAINING FINISHED")
print("=" * 60)