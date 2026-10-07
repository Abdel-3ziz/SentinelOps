import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# ==========================================
# 1. Load Test Data
# ==========================================

test_df = pd.read_csv("data/processed/test.csv")

X_test = test_df.drop(columns=["Label"])
y_test = test_df["Label"]


# ==========================================
# 2. Load Trained Model
# ==========================================

model = joblib.load("models/random_forest.pkl")


# ==========================================
# 3. Make Predictions
# ==========================================

print("Making predictions...")

y_pred = model.predict(X_test)


# ==========================================
# 4. Create Confusion Matrix
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=model.classes_
)


# ==========================================
# 5. Display Confusion Matrix
# ==========================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

fig, ax = plt.subplots(figsize=(14, 14))

disp.plot(
    ax=ax,
    xticks_rotation=90
)

plt.title("Random Forest - Confusion Matrix")
plt.tight_layout()

plt.show()