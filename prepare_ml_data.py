import pandas as pd

# Load network dataset
data = pd.read_csv("network_data.csv")

# Sort data by cell and hour
data = data.sort_values(["cell_id", "hour"])

# Create previous-hour traffic feature
data["previous_traffic_mbps"] = (
    data.groupby("cell_id")["traffic_mbps"].shift(1)
)

# Create next-hour traffic as prediction target
data["target_traffic_mbps"] = (
    data.groupby("cell_id")["traffic_mbps"].shift(-1)
)

# Remove rows with missing values
ml_data = data.dropna().copy()

# Select input features
features = [
    "hour",
    "capacity_mbps",
    "traffic_mbps",
    "previous_traffic_mbps",
    "load_percent"
]

X = ml_data[features]

# Select prediction target
y = ml_data["target_traffic_mbps"]

# Save prepared dataset
ml_data.to_csv("results/ml_dataset.csv", index=False)

print("ML dataset preparation completed!")
print("Number of samples:", len(ml_data))

print("\nInput Features:")
print(X.head())

print("\nPrediction Target:")
print(y.head())

print("\nDataset saved as results/ml_dataset.csv")