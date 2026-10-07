import pandas as pd
import joblib
from sklearn.metrics import classification_report, accuracy_score


# ==========================================
# 1. Load Test Data
# ==========================================

test_path = "data/processed/test.csv"

print("=" * 60)
print("RANDOM FOREST EVALUATION")
print("=" * 60)

print("\nLoading test data...")

test_df = pd.read_csv(test_path)

print(f"Test data shape: {test_df.shape}")


# ==========================================
# 2. Separate Features and Label
# ==========================================

X_test = test_df.drop(columns=["Label"])
y_test = test_df["Label"]

print(f"\nX_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")


# ==========================================
# 3. Load Trained Model
# ==========================================

print("\nLoading trained model...")

model = joblib.load("models/random_forest.pkl")

print("Model loaded successfully.")


# ==========================================
# 4. Make Predictions
# ==========================================

print("\nMaking predictions...")

y_pred = model.predict(X_test)

print("Predictions completed.")


# ==========================================
# 5. Accuracy
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(f"{accuracy:.4f}")


# ==========================================
# 6. Classification Report
# ==========================================

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


print("\n" + "=" * 60)
print("EVALUATION FINISHED")
print("=" * 60)