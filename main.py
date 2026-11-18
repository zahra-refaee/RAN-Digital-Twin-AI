
import random
import csv

cells = [
    {"cell_id": "Cell_001", "capacity_mbps": 100, "base_traffic": 45},
    {"cell_id": "Cell_002", "capacity_mbps": 120, "base_traffic": 55},
    {"cell_id": "Cell_003", "capacity_mbps": 80, "base_traffic": 35}
]

network_data = []

for hour in range(24):

    # Daily traffic pattern
    if 0 <= hour < 6:
        traffic_factor = 0.35
    elif 6 <= hour < 12:
        traffic_factor = 0.70
    elif 12 <= hour < 18:
        traffic_factor = 0.85
    else:
        traffic_factor = 1.0

    for cell in cells:

        traffic = (
            cell["base_traffic"] * traffic_factor
            + random.uniform(-5, 5)
        )

        traffic = max(0, traffic)

        load = traffic / cell["capacity_mbps"] * 100

        if load >= 90:
            status = "CONGESTED"
        elif load >= 70:
            status = "WARNING"
        else:
            status = "NORMAL"

        record = {
            "hour": hour,
            "cell_id": cell["cell_id"],
            "capacity_mbps": cell["capacity_mbps"],
            "traffic_mbps": round(traffic, 2),
            "load_percent": round(load, 2),
            "status": status
        }

        network_data.append(record)

with open("network_data.csv", "w", newline="") as file:

    fieldnames = [
        "hour",
        "cell_id",
        "capacity_mbps",
        "traffic_mbps",
        "load_percent",
        "status"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(network_data)

print("24-hour RAN simulation completed!")
print("Total records:", len(network_data))
print("Dataset saved as network_data.csv")
