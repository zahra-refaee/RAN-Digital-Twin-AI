import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("results/optimization_results.csv")

plt.figure(figsize=(9, 5))

plt.bar(
    data["cell_id"],
    data["load_before"],
    width=0.4,
    label="Before"
)

plt.bar(
    data["cell_id"],
    data["load_after"],
    width=0.4,
    label="After"
)

plt.ylabel("Cell Load (%)")
plt.title("RAN Load Balancing Results")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("results/optimization_comparison.png")
plt.show()