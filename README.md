# 📊 Capstone Project I - Mutual Fund Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![ETL](https://img.shields.io/badge/ETL-Data%20Ingestion-orange)
![Status](https://img.shields.io/badge/Status-Day%201%20Completed-brightgreen)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)

## 🚀 Project Overview

This project is part of **Capstone Project I - Mutual Fund Analytics** for Bluestock Fintech.

The main objective of Day 1 is to set up the project structure, load mutual fund datasets, fetch live NAV data from MFAPI, validate AMFI scheme codes, and generate initial data quality reports.

---

## 📅 Day 1: Project Setup + Data Ingestion

### ✅ Completed Tasks

* Created project folder structure
* Initialized Git repository
* Installed required Python dependencies
* Created `requirements.txt`
* Loaded all 10 provided CSV datasets using Pandas
* Printed `.shape`, `.dtypes`, and `.head()` for each dataset
* Explored `fund_master` dataset
* Printed unique fund houses, categories, and sub-categories
* Validated AMFI scheme codes between `fund_master` and `nav_history`
* Fetched live NAV data from MFAPI
* Saved live NAV data as raw CSV files
* Generated data quality summary reports
* Committed and pushed Day 1 work to GitHub

---

## 📁 Project Folder Structure

```text
mutual-fund-analytics/
├── data/
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   ├── 03_aum_by_fund_house.csv
│   │   ├── 04_monthly_sip_inflows.csv
│   │   ├── 05_category_inflows.csv
│   │   ├── 06_industry_folio_count.csv
│   │   ├── 07_scheme_performance.csv
│   │   ├── 08_investor_transactions.csv
│   │   ├── 09_portfolio_holdings.csv
│   │   ├── 10_benchmark_indices.csv
│   │   └── live_nav/
│   └── processed/
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
└── README.md
```

---

## 📦 Datasets Used

| No. | Dataset Name                   | Description                  |
| --- | ------------------------------ | ---------------------------- |
| 1   | `01_fund_master.csv`           | Mutual fund master data      |
| 2   | `02_nav_history.csv`           | Historical NAV data          |
| 3   | `03_aum_by_fund_house.csv`     | AUM data by fund house       |
| 4   | `04_monthly_sip_inflows.csv`   | Monthly SIP inflow data      |
| 5   | `05_category_inflows.csv`      | Category-wise inflow data    |
| 6   | `06_industry_folio_count.csv`  | Industry folio count data    |
| 7   | `07_scheme_performance.csv`    | Scheme performance metrics   |
| 8   | `08_investor_transactions.csv` | Investor transaction records |
| 9   | `09_portfolio_holdings.csv`    | Portfolio holdings data      |
| 10  | `10_benchmark_indices.csv`     | Benchmark index data         |

---

## 🛠️ Technologies Used

| Tool / Library | Purpose                   |
| -------------- | ------------------------- |
| Python         | Core programming language |
| Pandas         | Data loading and analysis |
| NumPy          | Numerical operations      |
| Requests       | API data fetching         |
| Matplotlib     | Data visualization        |
| Seaborn        | Statistical visualization |
| Plotly         | Interactive visualization |
| SQLAlchemy     | Database connectivity     |
| SciPy          | Scientific computing      |

---

## ⚙️ Setup Instructions

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Day 1 Scripts

### Run data ingestion

```bash
python data_ingestion.py
```

### Run live NAV fetch

```bash
python live_nav_fetch.py
```

---

## 📊 Generated Reports

| Report                                 | Description                        |
| -------------------------------------- | ---------------------------------- |
| `reports/data_ingestion_summary.csv`   | Summary of loaded CSV files        |
| `reports/data_quality_summary.txt`     | Data quality observations          |
| `reports/scheme_code_validation.csv`   | AMFI code validation results       |
| `reports/live_nav_metadata.csv`        | Live NAV API metadata              |
| `reports/live_nav_failed_requests.csv` | Failed API request details, if any |

---

## 🔎 Key Data Quality Findings

* All 10 provided CSV datasets were successfully loaded using Pandas.
* The `fund_master` dataset contains fund house, category, sub-category, plan, benchmark, expense ratio, manager, and risk classification details.
* The dataset uses `risk_category` as the risk classification column.
* AMFI scheme codes were validated between `fund_master` and `nav_history`.
* Some assigned MFAPI scheme codes returned different scheme names than expected, so they were recorded as data-quality anomalies.
* The assigned code `125497` was mentioned as HDFC Top 100 Direct in the task, but MFAPI returned a different scheme name during validation.

---

## 🌐 MFAPI Live NAV Fetch

Live NAV data was fetched from:

```text
https://api.mfapi.in/mf/{scheme_code}
```

Fetched schemes:

| Assigned Fund       | Scheme Code | Validation Status |
| ------------------- | ----------: | ----------------- |
| HDFC Top 100 Direct |      125497 | Mismatch found    |
| SBI Bluechip        |      119551 | Mismatch found    |
| ICICI Bluechip      |      120503 | Mismatch found    |
| Nippon Large Cap    |      118632 | Matched           |
| Axis Bluechip       |      119092 | Mismatch found    |
| Kotak Bluechip      |      120841 | Mismatch found    |

---

## 🧾 Git Commit

```bash
git add .
git commit -m "Day 1: Data ingestion complete"
git branch -M main
git push -u origin main
```

---

## 🔗 Repository

```text
https://github.com/bellana-upendra/mutual-fund-analytics
```

---

## 👤 Author

**Bellana Upendra**
B.Tech CSE - Artificial Intelligence and Machine Learning
GitHub: [bellana-upendra](https://github.com/bellana-upendra)

---

## ✅ Status

**Day 1 Completed Successfully**


---

# 📅 Day 2: Data Cleaning + SQLite Database Design

## ✅ Completed Tasks

* Cleaned all 10 mutual fund datasets
* Parsed date columns into proper datetime format
* Removed duplicate records
* Validated NAV values greater than 0
* Forward-filled missing NAV values for holidays/weekends
* Standardized transaction types such as SIP, Lumpsum, and Redemption
* Validated transaction amount values greater than 0
* Fixed transaction date formats
* Checked and standardized KYC status values
* Converted scheme performance return columns into numeric format
* Checked expense ratio range between 0.1% and 2.5%
* Created SQLite database: `bluestock_mf.db`
* Loaded all cleaned datasets into SQLite tables
* Verified row counts between cleaned CSV files and SQLite database tables
* Created SQL schema file: `sql/schema.sql`
* Created analytical SQL queries file: `sql/queries.sql`
* Created data dictionary: `reports/data_dictionary.md`
* Committed and pushed Day 2 work to GitHub

---

## 📁 Day 2 Updated Project Structure

```text
mutual-fund-analytics/
├── data/
│   ├── raw/
│   └── processed/
│       ├── 01_fund_master_clean.csv
│       ├── 02_nav_history_clean.csv
│       ├── 03_aum_by_fund_house_clean.csv
│       ├── 04_monthly_sip_inflows_clean.csv
│       ├── 05_category_inflows_clean.csv
│       ├── 06_industry_folio_count_clean.csv
│       ├── 07_scheme_performance_clean.csv
│       ├── 08_investor_transactions_clean.csv
│       ├── 09_portfolio_holdings_clean.csv
│       └── 10_benchmark_indices_clean.csv
│
├── notebooks/
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
├── reports/
│   ├── data_dictionary.md
│   ├── data_ingestion_summary.csv
│   ├── data_quality_summary.txt
│   ├── scheme_code_validation.csv
│   ├── live_nav_metadata.csv
│   └── live_nav_failed_requests.csv
│
├── bluestock_mf.db
├── data_ingestion.py
├── live_nav_fetch.py
├── data_cleaning.py
├── load_database.py
├── requirements.txt
└── README.md
```

---

## 🧹 Data Cleaning Summary

| Dataset                        | Cleaning Performed                                                                        |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| `01_fund_master.csv`           | Removed duplicates and standardized column names                                          |
| `02_nav_history.csv`           | Parsed dates, sorted by AMFI code and date, forward-filled missing NAV, validated NAV > 0 |
| `03_aum_by_fund_house.csv`     | Removed duplicates and standardized column names                                          |
| `04_monthly_sip_inflows.csv`   | Removed duplicates and standardized column names                                          |
| `05_category_inflows.csv`      | Removed duplicates and standardized column names                                          |
| `06_industry_folio_count.csv`  | Removed duplicates and standardized column names                                          |
| `07_scheme_performance.csv`    | Converted returns to numeric, checked expense ratio range, flagged anomalies              |
| `08_investor_transactions.csv` | Standardized transaction types, validated amount > 0, fixed dates, checked KYC status     |
| `09_portfolio_holdings.csv`    | Removed duplicates and standardized column names                                          |
| `10_benchmark_indices.csv`     | Removed duplicates and standardized column names                                          |

---

## 🗄️ SQLite Database

Database created:

```text
bluestock_mf.db
```

All 10 cleaned CSV files were loaded successfully into SQLite tables.

---

## ✅ Row Count Verification

| Table Name                 | CSV Rows | Database Rows |
| -------------------------- | -------: | ------------: |
| `01_fund_master`           |       40 |            40 |
| `02_nav_history`           |    46000 |         46000 |
| `03_aum_by_fund_house`     |       90 |            90 |
| `04_monthly_sip_inflows`   |       48 |            48 |
| `05_category_inflows`      |      144 |           144 |
| `06_industry_folio_count`  |       21 |            21 |
| `07_scheme_performance`    |       40 |            40 |
| `08_investor_transactions` |    32778 |         32778 |
| `09_portfolio_holdings`    |      322 |           322 |
| `10_benchmark_indices`     |     8050 |          8050 |

---

## 🧾 SQL Files Created

| File              | Description                                               |
| ----------------- | --------------------------------------------------------- |
| `sql/schema.sql`  | Contains SQLite schema design and CREATE TABLE statements |
| `sql/queries.sql` | Contains 10 analytical SQL queries                        |

---

## 📊 Analytical SQL Queries Included

The `queries.sql` file includes:

1. Fund master preview
2. Average NAV per month
3. Highest NAV funds
4. Top fund houses by AUM
5. Monthly SIP inflow trend
6. Category-wise inflows
7. Industry folio count summary
8. Funds with expense ratio below 1%
9. Transactions by state
10. Transaction type summary

---

## 📘 Data Dictionary

Created:

```text
reports/data_dictionary.md
```

The data dictionary includes:

* Table descriptions
* Business use of each dataset
* Cleaning rules applied
* Source references
* Final deliverables summary

---

## ▶️ Run Day 2 Scripts

Run data cleaning:

```bash
python data_cleaning.py
```

Load cleaned data into SQLite:

```bash
python load_database.py
```

---

## 🧾 Day 2 Git Commit

```bash
git add .
git commit -m "Day 2: Cleaned data + SQLite DB loaded"
git push
```

---

## ✅ Day 2 Status

Day 2 Completed Successfully.

---

