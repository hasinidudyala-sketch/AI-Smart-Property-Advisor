# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 3 - MODEL TRAINING
# ============================================================

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor
)

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


print("="*70)
print("STEP 3 : MODEL TRAINING")
print("="*70)


# ============================================================
# LOAD TRAIN TEST DATA
# ============================================================

X_train = pd.read_csv(
    "data/X_train.csv"
)

X_test = pd.read_csv(
    "data/X_test.csv"
)

y_train = pd.read_csv(
    "data/y_train.csv"
)["Price"]

y_test = pd.read_csv(
    "data/y_test.csv"
)["Price"]


print("\nTraining Data :", X_train.shape)
print("Testing Data  :", X_test.shape)



# ============================================================
# MODELS
# ============================================================

models = {

    "Linear Regression":
        LinearRegression(),

    "Decision Tree":
        DecisionTreeRegressor(
            random_state=42
        ),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=200,
            random_state=42
        ),

    "Gradient Boosting":
        GradientBoostingRegressor(
            random_state=42
        ),

    "Extra Trees":
        ExtraTreesRegressor(
            n_estimators=200,
            random_state=42
        )
}



# ============================================================
# TRAIN AND EVALUATE
# ============================================================

results = []


for name, model in models.items():

    print("\nTraining :", name)


    model.fit(
        X_train,
        y_train
    )


    prediction = model.predict(
        X_test
    )


    r2 = r2_score(
        y_test,
        prediction
    )


    mae = mean_absolute_error(
        y_test,
        prediction
    )


    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            prediction
        )
    )


    print("R2 Score :", round(r2,4))


    results.append(
        [
            name,
            r2,
            mae,
            rmse,
            model
        ]
    )



# ============================================================
# COMPARISON TABLE
# ============================================================

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "R2 Score",
        "MAE",
        "RMSE",
        "Model Object"
    ]
)


print("\n")
print(
    results_df[
        [
            "Model",
            "R2 Score",
            "MAE",
            "RMSE"
        ]
    ]
)



# ============================================================
# SELECT BEST MODEL
# ============================================================

results_df = results_df.sort_values(
    by=[
        "R2 Score",
        "RMSE"
    ],
    ascending=[
        False,
        True
    ]
)


best_model_name = results_df.iloc[0]["Model"]

best_model = results_df.iloc[0]["Model Object"]



print("\n"+"="*70)

print("BEST MODEL")

print("="*70)

print("Model :", best_model_name)

print(
    "R2 Score :",
    round(
        results_df.iloc[0]["R2 Score"],
        4
    )
)



# ============================================================
# SAVE MODEL
# ============================================================

os.makedirs(
    "models",
    exist_ok=True
)


joblib.dump(
    best_model,
    "models/best_model.pkl"
)



print("\nModel Saved Successfully")

print(
    "Location : models/best_model.pkl"
)


print("="*70)

print("STEP 3 COMPLETED")

print("="*70)
