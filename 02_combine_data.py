import pandas as pd
import os

print("Loading YouTube datasets...")

# Load data for three countries
india = pd.read_csv("data/INvideos.csv")
usa = pd.read_csv("data/USvideos.csv")
great_britain = pd.read_csv("data/GBvideos.csv")

# Add country names
india["country"] = "India"
usa["country"] = "USA"
great_britain["country"] = "Great Britain"

print("All three datasets loaded successfully!")

# Combine all three datasets
combined = pd.concat(
    [india, usa, great_britain],
    ignore_index=True
)

print("\nAll datasets combined successfully!")
print("Total rows:", len(combined))
print("Total columns:", len(combined.columns))

print("\nRows by country:")
print(combined["country"].value_counts())

# Create output folder if it does not exist
os.makedirs("output", exist_ok=True)

# Save combined data
combined.to_csv("output/combined_youtube_data.csv", index=False)

print("\nCombined data saved successfully!")
print("File location: output/combined_youtube_data.csv")