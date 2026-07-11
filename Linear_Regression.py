# --- Applying Regression Algorithm: Linear Regression ---
print("--- Applying Linear Regression ---")

# Initialize the Linear Regression model
linear_model = LinearRegression()

# Train the model using the training data
linear_model.fit(X_train, y_train)
print("Linear Regression model trained successfully.")

# Make predictions on the test set
y_pred_lr = linear_model.predict(X_test)

# --- Evaluating the Model ---
print("\n--- Evaluating Linear Regression Model ---")
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print(f"Mean Squared Error (MSE): {mse_lr:.4f}")
print(f"R-squared (R2): {r2_lr:.4f}")

# --- Explaining Model Error Values ---
print("\n--- Explanation of Model Error Values ---")
print("**Mean Squared Error (MSE):**")
print("   - MSE measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value. A lower MSE indicates a better fit of the model to the data.")
print("   - Since the errors are squared, larger errors are penalized more heavily. The units of MSE are the square of the units of the target variable (in this case, square of RCACScore units).")

print("\n**R-squared (R2 Score):**")
print("   - R-squared represents the proportion of the variance in the dependent variable that is predictable from the independent variables. It's a measure of how well the model explains the variability of the target variable.")
print("   - An R2 score of 1 indicates that the model explains all the variability of the target variable, while an R2 score of 0 indicates that the model explains none of the variability.")
print("   - A higher R2 score (closer to 1) generally indicates a better fit.")
