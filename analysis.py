import pandas as pd
import numpy as np

# --- Step 1 & 2: Import the new dataset related to sustainability ---
file_path = '/content/WorldSustainabilityDataset.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Successfully imported data from: {file_path}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the path is correct.")
    df = pd.DataFrame() # Create an empty DataFrame to avoid errors later


if not df.empty:
    # --- Step 3: Note generalizations and analysis about the dataset, note relations ---

    print("\n--- Initial Dataset Overview ---")
    print("First 5 rows of the DataFrame (df.head()):")
    display(df.head())
    print(f"\nShape of the dataset (rows, columns): {df.shape}")

    print("\nColumn information and data types (df.info()):")
    df.info()

    print("\nDescriptive statistics for numerical columns (df.describe()):")
    display(df.describe())
