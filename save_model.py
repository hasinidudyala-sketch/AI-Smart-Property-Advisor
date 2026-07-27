# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 9 - SAVE BEST MODEL
# ============================================================

import os
import joblib

print("=" * 70)
print("STEP 9 : SAVE BEST MODEL")
print("=" * 70)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_FOLDER = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODEL_FOLDER, "best_model.pkl")

os.makedirs(MODEL_FOLDER, exist_ok=True)

# ============================================================
# CHECK MODEL
# ============================================================

if os.path.exists(MODEL_PATH):

    print("\n✓ Model already exists.")
    print(f"Location : {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    print("\nModel Information")
    print("-" * 70)
    print("Model Type :", type(model))

else:

    print("\n❌ best_model.pkl not found.")
    print("Run train_models.py first.")

print("\n" + "=" * 70)
print("STEP 9 COMPLETED")
print("=" * 70)
