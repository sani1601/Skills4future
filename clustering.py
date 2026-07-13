import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# --- 1. Load the dataset ---
file_path = '/content/QS World University Rankings 2025 (Top global universities).csv'
try:
    df_rankings = pd.read_csv(file_path, encoding='latin1') # Added encoding='latin1'
    print(f"Successfully loaded data from: {file_path}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the path is correct.")
    df_rankings = pd.DataFrame() # Create an empty DataFrame to avoid errors later
except UnicodeDecodeError:
    print(f"Error: UnicodeDecodeError when reading '{file_path}'. Trying with a different encoding might be necessary.")
    df_rankings = pd.DataFrame() # Create an empty DataFrame to avoid errors later

if not df_rankings.empty:
    print("\n--- Initial Data Overview ---")
    print("First 5 rows of the DataFrame:")
    display(df_rankings.head())
    print(f"\nShape of the dataset (rows, columns): {df_rankings.shape}")

    print("\nColumn information and data types:")
    df_rankings.info()

    print("\nDescriptive statistics for numerical columns:")
    display(df_rankings.describe())

    # --- 2. Initial Data Cleaning ---
    print("\n--- Data Cleaning ---")
    # Drop columns that are not relevant for clustering or have too many missing values
    # For this dataset, 'Region' might be too specific or 'URL' is not relevant.
    # Let's check for columns with a high percentage of missing values.
    missing_percentage = df_rankings.isnull().sum() / len(df_rankings) * 100
    cols_to_drop_high_nan = missing_percentage[missing_percentage > 50].index.tolist()
    
    # Also, 'URL' is likely not useful for clustering
    if 'URL' in df_rankings.columns and 'URL' not in cols_to_drop_high_nan:
        cols_to_drop_high_nan.append('URL')

    if cols_to_drop_high_nan:
        print(f"Dropping columns with >50% missing values or irrelevant: {cols_to_drop_high_nan}")
        df_cleaned = df_rankings.drop(columns=cols_to_drop_high_nan)
    else:
        df_cleaned = df_rankings.copy()
        print("No columns with >50% missing values or irrelevant found to drop (other than specified).")

    # Impute remaining numerical columns with median and categorical with mode
    for column in df_cleaned.columns:
        if df_cleaned[column].isnull().any():
            if df_cleaned[column].dtype == 'object':  # Categorical column
                mode_val = df_cleaned[column].mode()[0]
                df_cleaned[column].fillna(mode_val, inplace=True)
                print(f"Imputed categorical column '{column}' with mode: '{mode_val}'")
            else:  # Numerical column
                median_val = df_cleaned[column].median()
                df_cleaned[column].fillna(median_val, inplace=True)
                print(f"Imputed numerical column '{column}' with median: {median_val:.2f}")

    print("\nMissing values after handling:")
    display(df_cleaned.isnull().sum()[df_cleaned.isnull().sum() > 0]) # Should be empty or all zeros

    print("\n--- Cleaned DataFrame Sample (first 5 rows) ---")
    display(df_cleaned.head())
    print(f"Shape of the cleaned dataset: {df_cleaned.shape}")

    # --- 3. Identify numerical features for clustering ---
    # Exclude identifier columns and categorical columns that are not yet encoded
    numerical_features = df_cleaned.select_dtypes(include=np.number).columns.tolist()
    # Exclude 'Rank' if it's treated as an output or an identifier, not a feature for clustering universities based on their inherent characteristics
    if 'Rank' in numerical_features:
        numerical_features.remove('Rank')
    if 'Overall Score' in numerical_features:
        numerical_features.remove('Overall Score') # Often a composite score, not an independent feature

    print(f"\nNumerical features selected for clustering: {numerical_features}")
    
    # Also identify categorical features that need encoding
    categorical_features = df_cleaned.select_dtypes(include='object').columns.tolist()
    if 'University' in categorical_features:
        categorical_features.remove('University') # University name is an identifier

    print(f"Categorical features to encode: {categorical_features}")

    # --- 4. Scale numerical features and encode categorical features ---
    print("\n--- Data Preprocessing for Clustering ---")
    scaler = StandardScaler()
    df_scaled_numerical = pd.DataFrame(scaler.fit_transform(df_cleaned[numerical_features]), columns=numerical_features, index=df_cleaned.index)
    print("Numerical features scaled.")

    df_encoded_categorical = pd.get_dummies(df_cleaned[categorical_features], drop_first=True)
    print("Categorical features one-hot encoded.")

    # Combine preprocessed features
    df_preprocessed = pd.concat([df_scaled_numerical, df_encoded_categorical], axis=1)
    print("Combined scaled numerical and encoded categorical features.")

    print("\nPreprocessed Data Sample (first 5 rows):")
    display(df_preprocessed.head())
    print(f"Shape of the preprocessed dataset: {df_preprocessed.shape}")

    # --- 5. Determine Optimal Number of Clusters (Elbow Method) ---
    print("\n--- Determining Optimal Number of Clusters (Elbow Method) ---")
    sse = [] # Sum of squared errors
    k_range = range(1, 11) # Test k from 1 to 10
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) # n_init to suppress warning
        kmeans.fit(df_preprocessed)
        sse.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(k_range, sse, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Sum of Squared Errors (SSE)')
    plt.xticks(k_range)
    plt.grid(True)
    plt.show()

    print("The plot above shows the Sum of Squared Errors (SSE) for different numbers of clusters (K). The 'elbow point' in the graph (where the rate of decrease in SSE significantly changes) suggests an optimal number of clusters. Please examine the plot to choose an appropriate K.")
    
else:
    print("Data loading failed or DataFrame is empty, cannot proceed with clustering analysis.")
