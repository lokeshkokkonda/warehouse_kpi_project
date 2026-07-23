# Warehouse Operations & WMS Performance Analytics Engine

## Executive Summary & Business Problem
Fulfillment center managers often struggle with fragmented Warehouse Management System (WMS) logs that obscure operational bottlenecks across receiving, storage, and order picking. Without centralized KPI tracking, dock delays reduce sellable inventory availability, and unoptimized pick paths increase labor costs.

This project builds an automated end-to-end analytics engine that processes WMS transaction logs, calculates core fulfillment metrics, and exposes dynamic DAX measures for Power BI dashboarding.

---

## STAR Project Overview

- **Situation:** Distribution centers experience unmonitored dock-to-stock cycle times and zone-based picking productivity variations, leading to SLA breaches and higher labor costs.
- **Task:** Build an automated data pipeline and BI framework to audit fulfillment cycle times, picking accuracy, space utilization, and picker productivity across warehouse zones.
- **Action:** Developed Python scripts for event log generation and automated audit checks, modeled the schema in Power BI, and authored explicit DAX measures for dynamic reporting.
- **Result:** Created a centralized operational dashboard enabling fulfillment managers to identify bottlenecks, track LPPH labor productivity by zone, and enforce a 2.0-hour dock-to-stock SLA target.

---

## Data Pipeline Architecture

```mermaid
flowchart LR
    A[Raw WMS Event Log\ndata/raw/wms_event_log.csv] --> B[Python Audit Engine\nsrc/analyze_wms_kpis.py]
    B --> C[Processed KPI Summary\ndata/processed/warehouse_kpi_summary.xlsx]
    B --> D[Visual Productivity Chart\nreports/picking_productivity_chart.png]
    A --> E[Power BI Data Model]
    E --> F[Explicit DAX Measures\ndax_measures.txt]
    F --> G[Interactive Executive Dashboard]

    warehouse_kpi_project/
│
├── README.md                     <-- Project documentation
├── requirements.txt              <-- Python dependencies
├── .gitignore                    <-- Git exclusion rules
├── LICENSE                       <-- MIT License
├── dax_measures.txt              <-- Explicit DAX formulas
│
├── data/
│   ├── raw/
│   │   └── wms_event_log.csv     <-- Raw WMS event logs
│   └── processed/
│       └── warehouse_kpi_summary.xlsx
│
├── src/
│   ├── generate_wms_data.py      <-- Event log generator
│   └── analyze_wms_kpis.py       <-- Audit calculation engine
│
└── reports/
    └── picking_productivity_chart.png <-- Visual reports