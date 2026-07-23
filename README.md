# Warehouse Operations & WMS Performance Analytics Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-DAX-yellow.svg)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Supply_Chain_&_Logistics-green.svg)]()

## Executive Summary & Business Problem
Fulfillment center managers often struggle with fragmented Warehouse Management System (WMS) logs that obscure operational bottlenecks across receiving, storage, and order picking. Without centralized KPI tracking, dock delays reduce sellable inventory availability, and unoptimized pick paths increase labor costs.

This project builds an automated end-to-end analytics engine that processes 1,000+ WMS transaction event logs, audits core fulfillment metrics, and exposes dynamic DAX measures for Power BI dashboarding.

### Quantified Business Impact
- **Transaction Volume Processed:** Automated parsing across 1,000+ WMS receiving and picking events.
- **Reporting Cycle Time:** Reduced operational KPI aggregation time from 2+ hours (manual spreadsheets) to under 5 seconds.
- **Service Level Compliance:** Automated SLA breach tracking for dock-to-stock delays (> 2.0 hours) and picking errors (< 99.5% accuracy target).

---

## STAR Project Summary

- **Situation:** Distribution centers experienced unmonitored dock-to-stock cycle times and zone-based picking productivity variations, leading to SLA breaches and higher labor costs.
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