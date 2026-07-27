# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 7 - PROPERTY RECOMMENDATION SYSTEM
# ============================================================

import pandas as pd

print("=" * 70)
print("STEP 7 : PROPERTY RECOMMENDATION SYSTEM")
print("=" * 70)

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(
    r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data\Enhanced_Smart_House_Price_Dataset.csv"
)

print("\nDataset Loaded Successfully")

# ============================================================
# USER REQUIREMENTS
# ============================================================

budget = 600000

minimum_bedrooms = 3

minimum_bathrooms = 2

print("\nUSER REQUIREMENTS")
print("-" * 70)

print(f"Maximum Budget    : ₹ {budget:,.2f}")
print(f"Minimum Bedrooms  : {minimum_bedrooms}")
print(f"Minimum Bathrooms : {minimum_bathrooms}")

# ============================================================
# FILTER PROPERTIES
# ============================================================

recommended_properties = df[
    (df["Price"] > 0) &
    (df["Price"] <= budget) &
    (df["Bedrooms"] >= minimum_bedrooms) &
    (df["Bathrooms"] >= minimum_bathrooms)
]

recommended_properties = recommended_properties.sort_values(
    by="Price"
)

# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 70)
print("RECOMMENDED PROPERTIES")
print("=" * 70)

if recommended_properties.empty:

    print("No properties found for the selected criteria.")

else:

    print(f"Total Matching Properties : {len(recommended_properties)}\n")

    print(
        recommended_properties[
            [
                "SquareFeet",
                "Bedrooms",
                "Bathrooms",
                "Neighborhood",
                "YearBuilt",
                "Price"
            ]
        ].head(10)
    )

print("\nRecommendation Completed Successfully!")

print("=" * 70)
print("STEP 7 COMPLETED")
print("=" * 70)
