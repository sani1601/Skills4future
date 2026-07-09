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

print("\n--- Relations of Features (Correlation Analysis) ---")
# Select numerical columns for correlation analysis. This will capture relationships
# between different sustainability indicators if they are numerical.
numerical_cols = df.select_dtypes(include=np.number).columns.tolist()

if len(numerical_cols) > 1:
    print("Correlation matrix for numerical features (first 10 rows/columns):")
    # Computing correlation on a subset of the DataFrame to manage NaN values and relevance
    display(df[numerical_cols].corr().head(10).iloc[:, :10])
    print("\nObservations from correlation:\n")
    print("- High positive correlations (close to 1) between features suggest they move in the same direction. For example, 'population' and 'gdp' might be highly correlated with certain resource consumption metrics.")
    print("- High negative correlations (close to -1) indicate an inverse relationship. For instance, increased renewable energy adoption might correlate negatively with fossil fuel consumption.")
    print("- Correlations close to 0 suggest little to no linear relationship between the features.")
    print("- We will need to interpret these correlations based on the specific meaning of each column in the 'WorldSustainabilityDataset.csv'.")
else:
    print("Not enough numerical columns for meaningful correlation analysis in the new dataset.")

# --- Step 4: Handle null values according to understanding of dataset ---

print("\n--- Handling Null Values ---")
# Identify missing values before handling
missing_values_before = df.isnull().sum()
print("Missing values before handling (columns with > 0 missing values):\n")
display(missing_values_before[missing_values_before > 0].sort_values(ascending=False))

# Strategy for handling null values:
# 1. Drop columns with a very high percentage of missing values (e.g., > 70%),
#    as they might not be useful for analysis.
# 2. For remaining numerical columns, impute with the median. Median is robust to outliers.
# 3. For categorical columns, impute with the mode.

# Calculate percentage of missing values for each column
missing_percentage = (df.isnull().sum() / len(df)) * 100

# Drop columns that have more than 70% missing values
cols_to_drop_high_nan = missing_percentage[missing_percentage > 70].index.tolist()
if cols_to_drop_high_nan:
    print(f"\nDropping columns with > 70% missing values: {cols_to_drop_high_nan}")
    df_cleaned = df.drop(columns=cols_to_drop_high_nan)
else:
    df_cleaned = df.copy()
    print("\nNo columns with > 70% missing values were found to drop.")

# Impute remaining numerical columns with their median
for col in df_cleaned.select_dtypes(include=np.number).columns:
    if df_cleaned[col].isnull().any():
        median_val = df_cleaned[col].median()
        df_cleaned[col].fillna(median_val, inplace=True)
        print(f"Imputed missing values in numerical column '{col}' with median: {median_val:.2f}")

# Impute remaining categorical/object columns with their mode
for col in df_cleaned.select_dtypes(include='object').columns:
    if df_cleaned[col].isnull().any():
        # .mode()[0] is used because mode can return multiple values if there's a tie
        mode_val = df_cleaned[col].mode()[0]
        df_cleaned[col].fillna(mode_val, inplace=True)
        print(f"Imputed missing values in categorical column '{col}' with mode: '{mode_val}'")

print("\nMissing values after handling (should be 0 for most, except potentially new cols added later):")
missing_values_after = df_cleaned.isnull().sum()
display(missing_values_after[missing_values_after > 0])

print("\n--- Cleaned DataFrame Sample (first 5 rows) ---")
display(df_cleaned.head())
print(f"\nShape of the cleaned dataset: {df_cleaned.shape}")
