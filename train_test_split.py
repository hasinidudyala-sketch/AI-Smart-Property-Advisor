# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 2 : FEATURE ENGINEERING + TRAIN TEST SPLIT
# ============================================================

import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


print("="*70)
print("STEP 2 : FEATURE ENGINEERING + TRAIN TEST SPLIT")
print("="*70)


# ============================================================
# LOAD DATASET
# ============================================================

dataset_path = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data\Enhanced_Smart_House_Price_Dataset.csv"


df = pd.read_csv(dataset_path)


print("\nDataset Loaded Successfully")
print("Dataset Shape :", df.shape)



# ============================================================
# FEATURE ENGINEERING
# ============================================================

CURRENT_YEAR = 2026


# House Age

df["HouseAge"] = (
    CURRENT_YEAR - df["YearBuilt"]
)



# House Size Category

df["HouseSizeCategory"] = pd.cut(

    df["SquareFeet"],

    bins=[
        0,
        1000,
        2000,
        3500,
        float("inf")
    ],

    labels=[
        "Small",
        "Medium",
        "Large",
        "Luxury"
    ]

)



# Family Suitability Score

df["FamilySuitabilityScore"] = (

    df["Bedrooms"] * 3 +

    df["Bathrooms"] * 2

)



# Property Score

df["PropertyScore"] = (

    df["SquareFeet"]/100

    +

    df["Bedrooms"]*10

    +

    df["Bathrooms"]*8

    -

    df["HouseAge"]*0.5

)



# Neighborhood Average Price

df["NeighborhoodAveragePrice"] = (

    df.groupby("Neighborhood")["Price"]

    .transform("mean")

)



# Investment Score

df["InvestmentScore"] = (

    df["NeighborhoodAveragePrice"]

    /

    df["Price"]

).round(2)



# Value For Money Score

df["ValueForMoneyScore"] = (

    df["SquareFeet"]

    /

    df["Price"]

) * 100000



print("\nFeature Engineering Completed")



# ============================================================
# LABEL ENCODING
# ============================================================


categorical_columns = df.select_dtypes(

    include=["object","category"]

).columns



for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(

        df[column].astype(str)

    )



print("Categorical Encoding Completed")



# ============================================================
# FEATURES AND TARGET
# ============================================================


X = df.drop(

    [

        "Price"

    ],

    axis=1

)


y = df["Price"]



# ============================================================
# TRAIN TEST SPLIT
# ============================================================


X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.30,

    random_state=42

)



# ============================================================
# SAVE DATA
# ============================================================


data_path = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data"


X_train.to_csv(

    os.path.join(data_path,"X_train.csv"),

    index=False

)


X_test.to_csv(

    os.path.join(data_path,"X_test.csv"),

    index=False

)


y_train.to_csv(

    os.path.join(data_path,"y_train.csv"),

    index=False

)


y_test.to_csv(

    os.path.join(data_path,"y_test.csv"),

    index=False

)



print("\nTraining Data :", X_train.shape)

print("Testing Data  :", X_test.shape)


print("\nSaved Files:")

print("✓ X_train.csv")

print("✓ X_test.csv")

print("✓ y_train.csv")

print("✓ y_test.csv")



print("\n"+"="*70)

print("STEP 2 COMPLETED SUCCESSFULLY")

print("="*70)

# ============================================================
# SAVE TRAIN TEST DATA
# ============================================================

import os

os.makedirs("data", exist_ok=True)

X_train.to_csv(
    "data/X_train.csv",
    index=False
)

X_test.to_csv(
    "data/X_test.csv",
    index=False
)

y_train.to_csv(
    "data/y_train.csv",
    index=False
)

y_test.to_csv(
    "data/y_test.csv",
    index=False
)


print("\nTrain Test Data Saved Successfully")

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)
