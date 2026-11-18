
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("results/ml_dataset.csv")

# Define features and target
features = [
    "hour",
    "capacity_mbps",
    "traffic_mbps",
    "previous_traffic_mbps",
    "load_percent"
]

X = data[features]
y = data["target_traffic_mbps"]

# Split dataset (same settings as training)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict traffic
predictions = model.predict(X_test)

# Create comparison dataframe
comparison = pd.DataFrame({
    "Actual Traffic": y_test.values,
    "Predicted Traffic": predictions
})

# Plot actual vs predicted
plt.figure(figsize=(10, 5))

plt.plot(
    comparison["Actual Traffic"].values,
    marker="o",
    label="Actual Traffic"
)

plt.plot(
    comparison["Predicted Traffic"].values,
    marker="x",
    label="Predicted Traffic"
)

plt.title("Actual vs Predicted RAN Traffic")
plt.xlabel("Test Sample")
plt.ylabel("Traffic (Mbps)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("results/prediction_comparison.png")
plt.show()

print("Prediction comparison completed!")
print(comparison.round(2))
