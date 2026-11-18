import pandas as pd

# Load network dataset
data = pd.read_csv("network_data.csv")

# Calculate statistics for each cell
report = data.groupby("cell_id").agg(
    average_load=("load_percent", "mean"),
    maximum_load=("load_percent", "max"),
    congested_intervals=("status", lambda x: (x == "CONGESTED").sum()),
    total_intervals=("status", "count")
)

# Calculate congestion percentage
report["congestion_percentage"] = (
    report["congested_intervals"] / report["total_intervals"]
) * 100

# Round numerical results
report = report.round(2)

# Display the report
print("\n===== RAN NETWORK PERFORMANCE REPORT =====")
print(report)

# Save report as CSV
report.to_csv("results/network_report.csv")

print("\nReport saved successfully!")