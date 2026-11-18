import pandas as pd
import matplotlib.pyplot as plt

# Load network dataset
data = pd.read_csv("network_data.csv")

# Create the plot
plt.figure(figsize=(10, 5))

# Plot load variation for each cell
for cell_id in data["cell_id"].unique():
    cell_data = data[data["cell_id"] == cell_id]

    plt.plot(
        cell_data["time_step"],
        cell_data["load_percent"],
        marker="o",
        label=cell_id
    )

# Add congestion thresholds
plt.axhline(y=70, linestyle="--", label="Warning Threshold")
plt.axhline(y=90, linestyle="--", label="Congestion Threshold")

plt.title("RAN Cell Load Variation Over Time")
plt.xlabel("Time Step")
plt.ylabel("Cell Load (%)")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Save the figure
plt.savefig("results/cell_load.png")

plt.show()