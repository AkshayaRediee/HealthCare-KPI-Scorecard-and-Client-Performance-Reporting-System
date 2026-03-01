# 📊 Healthcare Operations & Client Performance Analytics Dashboard

## 📌 Project Overview

This project demonstrates the design and implementation of a healthcare analytics reporting system built in **Databricks** using a **Bronze–Silver–Gold (Medallion) architecture**.


This project demonstrates the design and implementation of a healthcare analytics reporting system built in **Databricks** using a **Bronze–Silver–Gold (Medallion) architecture**.

The objective was to simulate how a data team supports:

- Operational KPI tracking
- Client/partner scorecards
- Cross-functional reporting
- Business decision-making
- Data consistency and transparency

⚠️ **Note:** All datasets used in this project are fully synthetic and were created for portfolio and educational purposes. No real patient or client data was used.


The solution processes healthcare operational data (patients, coaching sessions, support tickets, clients, and coaches) into business-ready KPI tables and interactive dashboards.

---

# 🏗 Architecture

This project follows a simplified **Medallion Architecture**:

## 🔹 Bronze Layer (Raw Data)
- Raw CSV files ingested into Delta tables
- No transformations applied
- Serves as the source of truth

This layer represents raw data ingestion directly from flat files (CSV-based data sources).

## 🔹 Silver Layer (Cleaned & Standardized)
- Standardized text fields using `LOWER()` and `TRIM()`
- Removed null primary keys
- Ensured consistent data formats
- Prepared tables for analysis

## 🔹 Gold Layer (Business KPIs)
- Aggregated operational metrics
- Created client-level scorecards
- Built dashboard-ready tables

All tables were stored as **Delta Lake tables** within Unity Catalog.

---
# 📂 Data Sources (Synthetic CSV Files)

The project uses the following synthetic CSV datasets:

| CSV File | Description |
|------------|------------|
| patients.csv | Simulated member demographic and enrollment data |
| clients.csv | Simulated client contract and segmentation information |
| coaches.csv | Simulated coaching staff details |
| coaching_sessions.csv | Simulated session activity records |
| support_tickets.csv | Simulated member support interactions |

These CSV files simulate real-world flat-file data ingestion commonly used in operational reporting systems.

# 📂 Datasets

| Table | Description |
|--------|------------|
| patients | Member demographic and enrollment data |
| clients | Client contract and segmentation information |
| coaches | Coaching staff details |
| coaching_sessions | Session activity records |
| support_tickets | Member support interactions |

---

# 📊 Key KPIs Implemented

## Internal Operational KPIs
- Total Active Members
- Total Completed Sessions
- No-Show Rate (%)
- Ticket Resolution Rate (%)

These metrics simulate how operations teams monitor engagement, utilization, and service performance.

## Client-Level Scorecard KPIs
For each client:
- Active Members
- Completed Sessions
- No-Show Rate
- Ticket Resolution Rate

This enables partner reporting and performance comparison across clients.

---

# 📈 Dashboard

Built using **Databricks Lakeview Dashboard**.

## Dashboard Sections

### 🔹 Run the Business (Executive View)
- 4 KPI tiles
- Real-time operational health metrics

### 🔹 Client Scorecard
- Bar chart: Active Members by Client
- Full Client Performance Table
- Interactive client filter

The dashboard supports segmentation and interactive performance monitoring.

---

# 🛠 SQL & Engineering Details
- CSV ingestion into Bronze Delta tables
- CTE-based aggregation for client-level KPIs
- `GROUP BY` aggregations across 9,000+ session records
- Conditional rate calculations using `CASE WHEN`
- Fact-to-dimension joins (patients → sessions → tickets → clients)
- Centralized KPI logic in Gold tables
- Delta format for structured storage and reliability


No advanced performance tuning was required due to moderate dataset size.

---

# 🧪 Data Quality Handling

Basic validation included:

- Removing null primary keys
- Standardizing text values for accurate grouping
- Ensuring consistent KPI calculations
- Centralizing metric definitions

This reduced discrepancies in reporting and improved consistency.

---

# 🎯 Business Impact (Simulated Environment)

This project demonstrates how a data analyst can:

- Reduce manual KPI calculation time
- Create a single source of truth for operational metrics
- Enable client-level reporting
- Improve cross-functional transparency
- Support faster operational decision-making

The architecture supports scalable expansion and scheduled refresh capability.

---

# 🔍 Technologies Used

- Databricks
- Delta Lake
- Unity Catalog
- SQL
- Lakeview Dashboards

---

# 🚀 Future Enhancements

Potential improvements include:

- Scheduled workflows (Databricks Jobs)
- Incremental data loading
- Partitioning and performance optimization
- Row-level security for client isolation
- Automated data quality checks
- Git integration and CI/CD
- Trend analysis (rolling 30-day KPIs)

---

# 👤 Author

Akshaya Reddy 
Healthcare Analytics Portfolio Project  
Databricks | SQL | Delta Lake
