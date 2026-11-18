import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("network_data.csv")

plt.figure(figsize=(10, 5))

for cell_id in data["cell_id"].unique():
    cell_data = data[data["cell_id"] == cell_id]

    plt.plot(
        cell_data["time_step"],
        cell_data["traffic_mbps"],
        marker="o",
        label=cell_id
    )

plt.title("RAN Traffic Variation Over Time")
plt.xlabel("Time Step")
plt.ylabel("Traffic (Mbps)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("results/traffic_trend.png")
plt.show()