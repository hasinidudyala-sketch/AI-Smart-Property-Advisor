# ==========================================================
# AI SMART PROPERTY ADVISOR
# STEP 1 - DATA PREPROCESSING
# ==========================================================

import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 1 : DATA PREPROCESSING")
print("=" * 70)


# ----------------------------------------------------------
# LOAD DATASET
# ----------------------------------------------------------

df = pd.read_csv("../data/Enhanced_Smart_House_Price_Dataset_New.csv")

print("\nDataset Loaded Successfully")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# ----------------------------------------------------------
# DATASET OVERVIEW
# ----------------------------------------------------------

print("\nFirst 5 Records")
print(df.head())


print("\nDataset Information")
df.info()


print("\nMissing Values")
print(df.isnull().sum())


print("\nDuplicate Rows :", df.duplicated().sum())


# ----------------------------------------------------------
# REMOVE DUPLICATES
# ----------------------------------------------------------

df.drop_duplicates(inplace=True)

# Reset index after duplicate removal
df.reset_index(drop=True, inplace=True)

print("\nDuplicate Rows Removed")
print("Current Shape :", df.shape)



# ----------------------------------------------------------
# CHECK AVAILABLE COLUMNS
# ----------------------------------------------------------

print("\nAvailable Columns:")
print(df.columns.tolist())



# ----------------------------------------------------------
# HANDLE MISSING VALUES
# ----------------------------------------------------------

print("\nHandling Missing Values...")

for column in df.columns:

    if df[column].dtype == "object":

        df[column].fillna(
            df[column].mode()[0],
            inplace=True
        )

    else:

        df[column].fillna(
            df[column].median(),
            inplace=True
        )


print("Missing Values Handled Successfully")



# ----------------------------------------------------------
# FEATURE ENGINEERING
# ----------------------------------------------------------

print("\nPerforming Feature Engineering...")


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
    df["Bathrooms"] * 2 +
    df["ParkingSpaces"] * 2 +
    df["Garden"] * 2
)



# Property Age

if "YearBuilt" in df.columns:

    current_year = 2026

    df["HouseAge"] = (
        current_year - df["YearBuilt"]
    )


print("Feature Engineering Completed")



# ----------------------------------------------------------
# LABEL ENCODING
# ----------------------------------------------------------

print("\nEncoding Categorical Columns...")


categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns


label_encoders = {}


for column in categorical_columns:

    le = LabelEncoder()

    df[column] = le.fit_transform(
        df[column].astype(str)
    )

    label_encoders[column] = le



print("Categorical Encoding Completed")



# ----------------------------------------------------------
# FINAL DATASET CHECK
# ----------------------------------------------------------

print("\nFinal Dataset Shape :", df.shape)


print("\nData Types")
print(df.dtypes)


print("\nStatistical Summary")
print(df.describe())



# ----------------------------------------------------------
# SAVE PROCESSED DATASET
# ----------------------------------------------------------

output_path = "../data/processed_property_data_New.csv"


df.to_csv(
    output_path,
    index=False
)


print("\nProcessed Dataset Saved Successfully")
print("Saved To :", output_path)



# ----------------------------------------------------------
# SAVE LABEL ENCODERS
# ----------------------------------------------------------

joblib.dump(
    label_encoders,
    "../models/label_encoders.pkl"
)


print("Label Encoders Saved Successfully")



# ----------------------------------------------------------
# DISPLAY PROCESSED DATA
# ----------------------------------------------------------

print("\nFirst 5 Processed Records")
print(df.head())



print("=" * 70)
print("STEP 1 COMPLETED SUCCESSFULLY")
print("=" * 70)
