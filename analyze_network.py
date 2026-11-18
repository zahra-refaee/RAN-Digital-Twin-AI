import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("network_data.csv")

average_traffic = data.groupby("hour")["traffic_mbps"].mean()

plt.figure(figsize=(10, 5))

plt.plot(
    average_traffic.index,
    average_traffic.values,
    marker="o"
)

plt.title("Average RAN Traffic Throughout the Day")
plt.xlabel("Hour of Day")
plt.ylabel("Average Traffic (Mbps)")
plt.xticks(range(24))
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("results/daily_traffic_pattern.png")
plt.show()

print("Daily traffic analysis completed!")