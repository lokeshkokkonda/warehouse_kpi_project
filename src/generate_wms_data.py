import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
num_records = 1000

# 1. Generate Order & Shipment IDs
order_ids = [f"ORD-{10000 + i}" for i in range(num_records)]
skus = [f"SKU-{np.random.randint(100, 150)}" for _ in range(num_records)]
pickers = [f"PKR-{np.random.randint(1, 10):02d}" for _ in range(num_records)]
zones = np.random.choice(['Zone_A_HighBay', 'Zone_B_Mezzanine', 'Zone_C_Bulk'], size=num_records, p=[0.5, 0.3, 0.2])

# 2. Simulate Timestamps (rounded to whole minutes to avoid microsecond clutter)
base_date = datetime(2026, 1, 1, 6, 0, 0)
received_times = [base_date + timedelta(minutes=int(i * 15) + int(np.random.randint(0, 30))) for i in range(num_records)]

putaway_times = []
for r_time in received_times:
    # Delays in whole minutes (4-7 hrs = 240-420 mins vs 1-2.5 hrs = 60-150 mins)
    delay_minutes = int(np.random.uniform(240, 420)) if np.random.rand() < 0.10 else int(np.random.uniform(60, 150))
    putaway_times.append(r_time + timedelta(minutes=delay_minutes))

# 3. Simulate Picking Accuracy & Labor Output
ordered_qty = np.random.randint(1, 20, size=num_records)
picked_qty = []
for qty in ordered_qty:
    if np.random.rand() < 0.02:
        picked_qty.append(qty + np.random.choice([-1, 1]))
    else:
        picked_qty.append(qty)

# 4. Build Pandas DataFrame with strict timestamp formatting
df = pd.DataFrame({
    'Order_ID': order_ids,
    'SKU': skus,
    'Pick_Zone': zones,
    'Picker_ID': pickers,
    'Received_Timestamp': [t.strftime('%Y-%m-%d %H:%M:%S') for t in received_times],
    'Putaway_Timestamp': [t.strftime('%Y-%m-%d %H:%M:%S') for t in putaway_times],
    'Ordered_Qty': ordered_qty,
    'Picked_Qty': picked_qty,
    'Pick_Duration_Minutes': np.random.randint(5, 25, size=num_records),
    'Location_Capacity_M3': 10.0,
    'Occupied_Volume_M3': np.random.uniform(6.0, 9.2, size=num_records).round(2)
})

# 5. Export clean dataset
df.to_csv('wms_event_log.csv', index=False)
print(f"Successfully generated {len(df)} clean WMS transaction records in wms_event_log.csv")