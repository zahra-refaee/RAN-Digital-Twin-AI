
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load prepared dataset
data = pd.read_csv("results/ml_dataset.csv")

# Define input features and target
features = [
    "hour",
    "capacity_mbps",
    "traffic_mbps",
    "previous_traffic_mbps",
    "load_percent"
]

X = data[features]
y = data["target_traffic_mbps"]

# Split data into training and testing sets
split_index = int(len(data) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


# Create the model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("===== TRAFFIC PREDICTION RESULTS =====")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 3))

# Save the trained model
import joblib

joblib.dump(model, "results/traffic_prediction_model.pkl")

print("\nModel saved successfully!")
