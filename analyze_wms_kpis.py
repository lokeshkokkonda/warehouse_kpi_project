import pandas as pd
import numpy as np

# 1. Load WMS Event Log
df = pd.read_csv('wms_event_log.csv')

# Explicit format parsing prevents dateutil ambiguity
df['Received_Timestamp'] = pd.to_datetime(df['Received_Timestamp'], format='%Y-%m-%d %H:%M:%S')
df['Putaway_Timestamp'] = pd.to_datetime(df['Putaway_Timestamp'], format='%Y-%m-%d %H:%M:%S')

# 2. Metric 1: Dock-to-Stock Cycle Time (Hours)
df['Dock_To_Stock_Hours'] = (
    (df['Putaway_Timestamp'] - df['Received_Timestamp']).dt.total_seconds() / 3600.0
).round(2)

avg_dock_to_stock = df['Dock_To_Stock_Hours'].mean().round(2)

# 3. Metric 2: Order Pick Accuracy Rate (%)
df['Is_Accurate_Pick'] = np.where(df['Ordered_Qty'] == df['Picked_Qty'], 1, 0)
pick_accuracy_pct = (df['Is_Accurate_Pick'].mean() * 100).round(2)

# 4. Metric 3: Lines Picked Per Hour (LPPH) by Zone
df['Pick_Duration_Hours'] = df['Pick_Duration_Minutes'] / 60.0
zone_lpph = df.groupby('Pick_Zone').agg(
    Total_Lines=('Order_ID', 'count'),
    Total_Hours=('Pick_Duration_Hours', 'sum')
).reset_index()

zone_lpph['LPPH'] = (zone_lpph['Total_Lines'] / zone_lpph['Total_Hours']).round(2)

# 5. Metric 4: Storage Cube Utilization (%)
df['Cube_Utilization_Pct'] = ((df['Occupied_Volume_M3'] / df['Location_Capacity_M3']) * 100).round(2)
avg_cube_utilization = df['Cube_Utilization_Pct'].mean().round(2)

# Output Summary Report
print("==================================================")
print("       WAREHOUSE OPERATIONS KPI SUMMARY REPORT    ")
print("==================================================")
print(f"1. Avg Dock-to-Stock Cycle Time : {avg_dock_to_stock} Hours (Target: < 2.0 Hrs)")
print(f"2. Overall Pick Accuracy Rate   : {pick_accuracy_pct}% (Target: > 99.5%)")
print(f"3. Avg Storage Cube Utilization  : {avg_cube_utilization}% (Target: 75% - 85%)")
print("\n4. Labor Productivity (LPPH) by Zone:")
print(zone_lpph[['Pick_Zone', 'Total_Lines', 'LPPH']].to_string(index=False))
print("==================================================")