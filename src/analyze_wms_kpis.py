import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 1. Load raw WMS event log dataset
df = pd.read_csv('data/raw/wms_event_log.csv')

# 2. Parse timestamps explicitly
df['Received_Timestamp'] = pd.to_datetime(df['Received_Timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['Putaway_Timestamp'] = pd.to_datetime(df['Putaway_Timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# 3. Compute Dock-to-Stock Cycle Time (Hours)
df['Dock_To_Stock_Hours'] = (df['Putaway_Timestamp'] - df['Received_Timestamp']).dt.total_seconds() / 3600.0

# 4. Compute Pick Accuracy Flag (1 if ordered quantity matches picked quantity)
df['Pick_Accuracy_Flag'] = np.where(df['Ordered_Qty'] == df['Picked_Qty'], 1, 0)

# 5. Aggregate Facility KPIs
avg_dock_to_stock = df['Dock_To_Stock_Hours'].mean()
overall_pick_accuracy = df['Pick_Accuracy_Flag'].mean() * 100
total_hours = df['Pick_Duration_Minutes'].sum() / 60.0
avg_lpph = len(df) / total_hours if total_hours > 0 else 0
avg_cube_utilization = (df['Occupied_Volume_M3'] / df['Location_Capacity_M3']).mean() * 100

# Save summary report
kpi_summary = pd.DataFrame({
    'Metric': ['Avg Dock-to-Stock (Hours)', 'Pick Accuracy (%)', 'Avg LPPH', 'Cube Utilization (%)'],
    'Value': [round(avg_dock_to_stock, 2), round(overall_pick_accuracy, 2), round(avg_lpph, 2), round(avg_cube_utilization, 2)]
})
kpi_summary.to_excel('data/processed/warehouse_kpi_summary.xlsx', index=False)

# 6. Generate LPPH Productivity Chart by Zone
zone_summary = df.groupby('Pick_Zone').agg(
    Total_Lines=('Order_ID', 'count'),
    Total_Hours=('Pick_Duration_Minutes', lambda x: x.sum() / 60.0)
).reset_index()

zone_summary['LPPH'] = zone_summary['Total_Lines'] / zone_summary['Total_Hours']

plt.figure(figsize=(9, 5))
ax = sns.barplot(data=zone_summary, x='Pick_Zone', y='LPPH', hue='Pick_Zone', palette='mako', legend=False)
plt.title('Average Picking Productivity (LPPH) by Warehouse Zone', fontsize=14, fontweight='bold')
plt.xlabel('Pick Zone', fontsize=12)
plt.ylabel('Lines Picked Per Hour (LPPH)', fontsize=12)

for p in ax.patches:
    height = p.get_height()
    if height > 0:
        ax.annotate(f'{height:.1f}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom', fontsize=10, fontweight='bold', xytext=(0, 3),
                    textcoords='offset points')

plt.tight_layout()
plt.savefig('reports/picking_productivity_chart.png', dpi=300)
plt.close()

print("WMS KPI analysis complete. Summaries saved to data/processed/ and chart saved to reports/")