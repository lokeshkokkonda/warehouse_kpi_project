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
    A[Raw WMS Event Log] --> B[Python Audit Engine]
    B --> C[Processed KPI Summary]
    B --> D[Visual Productivity Chart]
    A --> E[Power BI Data Model]
    E --> F[Explicit DAX Measures]
    F --> G[Interactive Dashboard]