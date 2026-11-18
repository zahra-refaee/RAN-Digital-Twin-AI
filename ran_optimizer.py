
import pandas as pd

data = pd.read_csv("network_data.csv")

current = data[data["hour"] == data["hour"].max()].copy()
current = current.reset_index(drop=True)

before = current["traffic_mbps"].copy()

# Target load: average network load
total_traffic = current["traffic_mbps"].sum()
total_capacity = current["capacity_mbps"].sum()
target_load = total_traffic / total_capacity

# Distribute traffic according to cell capacity
current["traffic_after"] = (
    current["capacity_mbps"] * target_load
)

current["load_before"] = (
    before / current["capacity_mbps"] * 100
)

current["load_after"] = (
    current["traffic_after"] / current["capacity_mbps"] * 100
)

print("BEFORE OPTIMIZATION")
print(current[["cell_id", "traffic_mbps", "load_before"]])

print("\nAFTER OPTIMIZATION")
print(current[["cell_id", "traffic_after", "load_after"]])

print("\nTotal traffic before:", round(before.sum(), 2))
print("Total traffic after:", round(current["traffic_after"].sum(), 2))

current.to_csv("results/optimization_results.csv", index=False)

print("\nOptimization completed!")
