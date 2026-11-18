
# RAN Digital Twin
# Session 7: Network Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Read network dataset
data = pd.read_csv("network_data.csv")

# Calculate average traffic per cell
average_traffic = data.groupby(
    "cell_id"
)["traffic_mbps"].mean()

# Create bar chart
plt.figure(figsize=(9, 5))

average_traffic.plot(
    kind="bar",
    title="Average Traffic per RAN Cell"
)

plt.xlabel("Cell ID")
plt.ylabel("Average Traffic (Mbps)")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

# Save chart
plt.savefig("results/average_traffic.png")

plt.show()
