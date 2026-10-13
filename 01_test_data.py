import pandas as pd
import os

print("Starting YouTube project...")

file_path = os.path.join("data", "INvideos.csv")

if os.path.exists(file_path):
    india = pd.read_csv(file_path)

    print("India dataset loaded successfully!")
    print("Number of rows:", len(india))
    print("Number of columns:", len(india.columns))

    print("\nColumn names:")
    print(india.columns.tolist())

    print("\nFirst 5 rows:")
    print(india.head())

    print("\nProject test completed!")
else:
    print("ERROR: INvideos.csv file not found.")
    print("Please check that INvideos.csv is inside the data folder.")