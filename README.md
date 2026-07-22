# Warehouse Operations & Interactive KPI Dashboard

## Overview
This project models fulfillment center throughput, storage volume efficiency, and labor productivity using 1,000 WMS (Warehouse Management System) event transaction logs. It evaluates operational SLAs, pick accuracy, and rack volume utilization across warehouse picking zones.

## Core Metrics & Target Benchmarks
- **Dock-to-Stock Cycle Time:** Time elapsed between inbound receiving and stock putaway ($< 2.0\text{ hours}$ SLA target).
- **Order Pick Accuracy Rate (%):** Proportion of error-free line items picked ($> 99.5\%$ target).
- **Lines Picked Per Hour (LPPH):** Labor throughput metric measuring picked order lines per labor hour completed.
- **Storage Cube Utilization (%):** Usable 3D rack space occupied by stored inventory ($75\% - 85\%$ optimal range).

## Repository Structure
- `generate_wms_data.py`: WMS event log dataset generator (with operational delays and picking noise).
- `wms_event_log.csv`: Transaction log containing 1,000 order picking and receiving timestamps.
- `analyze_wms_kpis.py`: Python audit script verifying operational benchmarks across warehouse zones.
- `dax_measures.txt`: Production DAX formulas used for dynamic filtering in Power BI.
- `README.md`: Functional documentation and metric definitions.

## How to Run
```cmd
python generate_wms_data.py
python analyze_wms_kpis.py