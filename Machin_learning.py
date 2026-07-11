# Import necessary libraries for model building
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("--- Defining Target and Feature Variables ---")
# For regression, let's choose 'RCACScore' as our target variable (y).
# All other relevant columns will be our features (X).

# Drop the target variable and any non-numeric/identifier columns that might have slipped through
# or were intentionally kept for context but not for modeling.
# We will also drop any columns that contain 'inf' values, which can occur after scaling if there were very small numbers.

# Identify 'RCACScore' as the target
if 'RCACScore' in df_bio_encoded.columns:
    target_variable = 'RCACScore'
    y = df_bio_encoded[target_variable]
    X = df_bio_encoded.drop(columns=[target_variable])
    
    # Drop columns that are entirely non-numeric or were identifiers not intended for modeling
    # and check for inf values in X after all previous processing
    X = X.select_dtypes(include=np.number) # Ensure all features are numeric
    
    # Replace infinite values with NaN and then impute them or drop columns if too many
    X.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    # Drop columns from X that might still have NaN values after selective imputation for ML
    # (e.g., if a column became all NaNs due to `on_bad_lines='skip'` or specific numeric conversions)
    X.dropna(axis=1, inplace=True)

    # Align X and y by ensuring they have the same index (important if rows were dropped)
    X, y = X.align(y, join='inner', axis=0)

    print(f"Target variable (y): '{target_variable}'")
    print(f"Shape of features (X): {X.shape}")
    print(f"Shape of target (y): {y.shape}")

    print("--- Splitting Data into Training and Testing Sets ---")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training features shape: {X_train.shape}")
    print(f"Testing features shape: {X_test.shape}")
    print(f"Training target shape: {y_train.shape}")
    print(f"Testing target shape: {y_test.shape}")
else:
    print("Error: 'RCACScore' not found in the preprocessed DataFrame. Cannot proceed with regression.")
