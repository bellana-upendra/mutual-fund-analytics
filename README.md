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
