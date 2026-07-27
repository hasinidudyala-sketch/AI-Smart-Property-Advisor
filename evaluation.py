# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 4 - MODEL EVALUATION
# ============================================================

import pandas as pd
import joblib

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

import numpy as np


print("="*70)
print("STEP 4 : MODEL EVALUATION")
print("="*70)


# ============================================================
# LOAD TEST DATA
# ============================================================

X_test = pd.read_csv(
    "data/X_test.csv"
)

y_test = pd.read_csv(
    "data/y_test.csv"
)


# Convert target dataframe to series

y_test = y_test["Price"]


print("\nTest Data Loaded")
print("X_test :", X_test.shape)
print("y_test :", y_test.shape)



# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model = joblib.load(
    "models/best_model.pkl"
)


print("\nModel Loaded Successfully")



# ============================================================
# PREDICTION
# ============================================================

y_pred = model.predict(
    X_test
)



# ============================================================
# EVALUATION METRICS
# ============================================================

r2 = r2_score(
    y_test,
    y_pred
)


mae = mean_absolute_error(
    y_test,
    y_pred
)


rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)



# ============================================================
# RESULTS
# ============================================================

print("\n"+"="*70)
print("MODEL PERFORMANCE")
print("="*70)


print(f"R² Score : {r2:.4f}")

print(f"MAE      : {mae:.2f}")

print(f"RMSE     : {rmse:.2f}")



# ============================================================
# SAVE RESULTS
# ============================================================

results = pd.DataFrame({

    "Metric":[
        "R2 Score",
        "MAE",
        "RMSE"
    ],

    "Value":[
        r2,
        mae,
        rmse
    ]

})


results.to_csv(
    "data/evaluation_results.csv",
    index=False
)



print("\nEvaluation Results Saved")

print("="*70)
print("STEP 4 COMPLETED")
print("="*70)
