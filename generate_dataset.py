import pandas as pd
import numpy as np

np.random.seed(42)

ROWS = 50000
CURRENT_YEAR = 2026

# ------------------------------------
# Basic Features
# ------------------------------------
square_feet = np.random.randint(600, 5001, ROWS)
bedrooms = np.random.randint(1, 7, ROWS)
bathrooms = np.random.randint(1, 6, ROWS)
floors = np.random.randint(1, 4, ROWS)
parking = np.random.randint(0, 5, ROWS)
year_built = np.random.randint(1990, 2026, ROWS)

neighborhood = np.random.choice(
    ["Urban", "Suburban", "Rural"],
    ROWS,
    p=[0.45, 0.40, 0.15]
)

property_type = np.random.choice(
    ["Apartment", "Villa", "Independent House"],
    ROWS,
    p=[0.45, 0.25, 0.30]
)

balcony = np.random.randint(0, 2, ROWS)
garden = np.random.randint(0, 2, ROWS)
lift = np.random.randint(0, 2, ROWS)
security = np.random.randint(0, 2, ROWS)

green_area = np.random.randint(1, 11, ROWS)
road = np.random.randint(1, 11, ROWS)
amenities = np.random.randint(1, 11, ROWS)
crime = np.random.randint(1, 11, ROWS)

# ------------------------------------
# Engineered Features
# ------------------------------------
house_age = CURRENT_YEAR - year_built
total_rooms = bedrooms + bathrooms

property_score = (
      square_feet * 0.08
    + amenities * 3000
    + green_area * 2000
    + road * 2500
    + security * 12000
    + lift * 9000
    - crime * 3000
    - house_age * 600
)

# ------------------------------------
# Category Effects
# ------------------------------------
neigh_bonus = {
    "Urban": 120000,
    "Suburban": 70000,
    "Rural": 25000
}

type_bonus = {
    "Apartment": 30000,
    "Villa": 180000,
    "Independent House": 100000
}

neigh_effect = np.array([neigh_bonus[x] for x in neighborhood])
type_effect = np.array([type_bonus[x] for x in property_type])

# ------------------------------------
# Target Variable (Price)
# ------------------------------------
noise = np.random.normal(0, 15000, ROWS)

price = (
      square_feet * 220
    + bedrooms * 30000
    + bathrooms * 20000
    + parking * 15000
    + neigh_effect
    + type_effect
    + property_score
    + noise
)

price = price.astype(int)

# ------------------------------------
# DataFrame
# ------------------------------------
df = pd.DataFrame({
    "SquareFeet": square_feet,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Floors": floors,
    "ParkingSpaces": parking,
    "YearBuilt": year_built,
    "Neighborhood": neighborhood,
    "PropertyType": property_type,
    "Balcony": balcony,
    "Garden": garden,
    "Lift": lift,
    "Security": security,
    "GreenAreaScore": green_area,
    "RoadConnectivity": road,
    "AmenitiesScore": amenities,
    "CrimeIndex": crime,
    "HouseAge": house_age,
    "TotalRooms": total_rooms,
    "PropertyScore": property_score.round(2),
    "Price": price
})

# ------------------------------------
# Save Dataset
# ------------------------------------
df.to_csv("Enhanced_Smart_House_Price_Dataset_New.csv", index=False)

print("=" * 60)
print("Dataset Generated Successfully!")
print("=" * 60)
print(df.head())
print()
print("Rows    :", len(df))
print("Columns :", len(df.columns))
print()
print("Saved as:")
print("Enhanced_Smart_House_Price_Dataset.csv")