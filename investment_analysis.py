# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 8 - INVESTMENT ANALYSIS
# ============================================================

import os
import pandas as pd
import joblib

print("=" * 70)
print("STEP 8 : INVESTMENT ANALYSIS")
print("=" * 70)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")

X_TEST_PATH = os.path.join(BASE_DIR, "data", "X_test.csv")

Y_TEST_PATH = os.path.join(BASE_DIR, "data", "y_test.csv")

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(MODEL_PATH)

print("\nModel Loaded Successfully")

# ============================================================
# LOAD TEST DATA
# ============================================================

X_test = pd.read_csv(X_TEST_PATH)

y_test = pd.read_csv(Y_TEST_PATH)

print("Test Data Loaded Successfully")

# ============================================================
# SELECT ONE PROPERTY
# ============================================================

sample_house = X_test.iloc[[0]]

actual_price = y_test.iloc[0]["Price"]

# ============================================================
# PREDICT PRICE
# ============================================================

predicted_price = model.predict(sample_house)[0]

# ============================================================
# INVESTMENT ANALYSIS
# ============================================================

average_market_price = y_test["Price"].mean()

investment_score = (
    average_market_price / predicted_price
) * 100

if predicted_price < average_market_price * 0.80:
    recommendation = "Excellent Investment"

elif predicted_price < average_market_price:
    recommendation = "Good Investment"

elif predicted_price <= average_market_price * 1.20:
    recommendation = "Average Investment"

else:
    recommendation = "Expensive Property"

# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 70)
print("INVESTMENT ANALYSIS RESULT")
print("=" * 70)

print(f"Average Market Price : ₹ {average_market_price:,.2f}")
print(f"Actual Price         : ₹ {actual_price:,.2f}")
print(f"Predicted Price      : ₹ {predicted_price:,.2f}")
print(f"Investment Score     : {investment_score:.2f}")
print(f"Recommendation       : {recommendation}")

print("\nInvestment Analysis Completed Successfully!")

print("=" * 70)
print("STEP 8 COMPLETED")
print("=" * 70)
