import pandas as pd

# 1. Import a sheet (CSV file) using pandas
file_path = '/content/8 Breast Cancer Wisconsin Diagnosis.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Successfully imported data from: {file_path}")
    print("\n--- First 5 rows of the DataFrame (df.head()) ---")
    print(df.head())
    print("\n" + "-" * 50 + "\n")

    # 2. Perform 10 methods of pandas on the DataFrame

    print("--- Applying 10 Pandas DataFrame Methods ---")

    # Method 1: .shape - Returns a tuple representing the dimensionality of the DataFrame
    print(f"1. DataFrame Shape (df.shape): {df.shape}")

    # Method 2: .info() - Prints a concise summary of a DataFrame
    print("\n2. DataFrame Info (df.info()):")
    df.info()

    # Method 3: .describe() - Generates descriptive statistics of numerical columns
    print("\n3. Descriptive Statistics (df.describe()):")
    print(df.describe())

    # Method 4: .columns - Returns the column labels of the DataFrame
    print(f"\n4. Column Names (df.columns): {df.columns.tolist()}")

    # Method 5: .dtypes - Returns a Series with the data type of each column
    print(f"\n5. Data Types (df.dtypes):\n{df.dtypes}")

    # Method 6: .isnull().sum() - Count of missing values per column
    print(f"\n6. Missing Values (df.isnull().sum()):\n{df.isnull().sum()}")

    # Method 7: .mean() - Returns the mean of the values for the requested axis
    # Exclude non-numeric columns for mean calculation
    print(f"\n7. Mean of numerical columns (df.mean()):\n{df.mean(numeric_only=True)}")

    # Method 8: .median() - Returns the median of the values for the requested axis
    # Exclude non-numeric columns for median calculation
    print(f"\n8. Median of numerical columns (df.median()):\n{df.median(numeric_only=True)}")

    # Method 9: .value_counts() - Returns a Series containing counts of unique values for a column
    # Using 'diagnosis' as a relevant column for value counts in this dataset
    if 'diagnosis' in df.columns:
        print(f"\n9. Value Counts for 'diagnosis' (df['diagnosis'].value_counts()):\n{df['diagnosis'].value_counts()}")
    else:
        print(f"\n9. 'diagnosis' column not found, skipping value_counts.")

    # Method 10: .corr() - Compute pairwise correlation of columns
    # Exclude non-numeric columns for correlation calculation
    print("\n10. Correlation Matrix (df.corr().head()):")
    print(df.corr(numeric_only=True).head())

    print("\n" + "-" * 50)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the path is correct.")
except Exception as e:
    print(f"An error occurred: {e}")
