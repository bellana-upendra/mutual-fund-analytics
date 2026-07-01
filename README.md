# 📊 Capstone Project I - Mutual Fund Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![ETL](https://img.shields.io/badge/ETL-Pipeline-orange)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Status](https://img.shields.io/badge/Status-Day%205%20Completed-brightgreen)

---

## 🚀 Project Overview

This project is part of **Capstone Project I - Mutual Fund Analytics** for Bluestock Fintech.

The objective of this capstone is to build an end-to-end mutual fund analytics solution covering:

* Data ingestion and cleaning
* SQLite database design
* Exploratory Data Analysis
* Fund performance analytics
* Advanced risk analytics
* Risk-based fund recommendation
* Interactive dashboard preparation
* Final reporting and presentation

---

## ✅ Final Deliverables Status

| ID | Deliverable                         | Status                | Location                                                           |
| -- | ----------------------------------- | --------------------- | ------------------------------------------------------------------ |
| D1 | ETL Pipeline Script                 | Completed             | `scripts/etl_pipeline.py`                                          |
| D2 | SQLite Database                     | Completed             | `data/db/bluestock_mf.db`                                          |
| D3 | EDA Notebook                        | Completed             | `notebooks/03_eda_analysis.ipynb`                                  |
| D4 | Performance Metrics Notebook + CSVs | Completed             | `notebooks/04_performance_analytics.ipynb`, `reports/performance/` |
| D5 | Interactive Dashboard               | Pending / In Progress | `dashboard/bluestock_mf.pbix`                                      |
| D6 | Advanced Analytics Notebook         | Completed             | `notebooks/05_advanced_analytics.ipynb`                            |
| D7 | Final Report + Slides               | Pending / In Progress | `reports/Final_Report.pdf`, `reports/Presentation.pptx`            |

---

## 📁 Final Project Folder Structure

```text
mutual-fund-analytics/
├── data/
│   ├── raw/
│   ├── processed/
│   │   ├── 01_fund_master_clean.csv
│   │   ├── 02_nav_history_clean.csv
│   │   ├── 03_aum_by_fund_house_clean.csv
│   │   ├── 04_monthly_sip_inflows_clean.csv
│   │   ├── 05_category_inflows_clean.csv
│   │   ├── 06_industry_folio_count_clean.csv
│   │   ├── 07_scheme_performance_clean.csv
│   │   ├── 08_investor_transactions_clean.csv
│   │   ├── 09_portfolio_holdings_clean.csv
│   │   └── 10_benchmark_indices_clean.csv
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── load_database.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── reports/
│   ├── charts/
│   ├── performance/
│   ├── advanced_analytics/
│   ├── dashboard_screenshots/
│   ├── data_dictionary.md
│   ├── data_ingestion_summary.csv
│   ├── data_quality_summary.txt
│   ├── scheme_code_validation.csv
│   ├── live_nav_metadata.csv
│   ├── live_nav_failed_requests.csv
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technologies Used

| Tool / Library   | Purpose                                 |
| ---------------- | --------------------------------------- |
| Python           | Core programming language               |
| Pandas           | Data loading, cleaning, and analysis    |
| NumPy            | Numerical calculations                  |
| Requests         | MFAPI live NAV fetching                 |
| Matplotlib       | Static chart generation                 |
| Seaborn          | Statistical visualization               |
| Plotly           | Interactive visualizations              |
| SQLite           | Local database storage                  |
| SQLAlchemy       | Database connectivity                   |
| SciPy            | Statistical and regression calculations |
| Jupyter Notebook | Analysis notebooks                      |
| Power BI         | Dashboard development                   |

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

## ▶️ Run ETL Pipeline

Run from the project root:

```bash
python scripts/etl_pipeline.py
```

The ETL pipeline performs:

1. Data ingestion
2. Data cleaning
3. SQLite schema creation
4. Cleaned CSV loading into SQLite
5. Row count validation

---

## ▶️ Run Individual Scripts

### Data ingestion

```bash
python scripts/data_ingestion.py
```

### Live NAV fetch

```bash
python scripts/live_nav_fetch.py
```

### Data cleaning

```bash
python scripts/data_cleaning.py
```

### Load cleaned data into SQLite

```bash
python scripts/load_database.py
```

### Check metrics output files

```bash
python scripts/compute_metrics.py
```

### Run fund recommender

```bash
python scripts/recommender.py --risk Low
python scripts/recommender.py --risk Moderate
python scripts/recommender.py --risk High
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

## 🧹 Data Cleaning Summary

The following cleaning steps were performed:

* Standardized column names
* Parsed date columns into proper datetime format
* Removed duplicate records
* Validated NAV values greater than 0
* Forward-filled missing NAV values for weekends and holidays
* Standardized transaction types such as SIP, Lumpsum, and Redemption
* Validated transaction amounts greater than 0
* Checked and standardized KYC status values
* Converted scheme performance return columns into numeric format
* Validated expense ratio range
* Exported all cleaned datasets to `data/processed/`

---

## 🗄️ SQLite Database

SQLite database created:

```text
data/db/bluestock_mf.db
```

All 10 cleaned datasets were loaded into SQLite tables.

> Note: The `.db` file is not committed to GitHub. It should be shared through Google Drive only.

---

## ✅ Row Count Verification

| Table Name                 | CSV Rows | DB Rows |
| -------------------------- | -------: | ------: |
| `01_fund_master`           |       40 |      40 |
| `02_nav_history`           |    46000 |   46000 |
| `03_aum_by_fund_house`     |       90 |      90 |
| `04_monthly_sip_inflows`   |       48 |      48 |
| `05_category_inflows`      |      144 |     144 |
| `06_industry_folio_count`  |       21 |      21 |
| `07_scheme_performance`    |       40 |      40 |
| `08_investor_transactions` |    32778 |   32778 |
| `09_portfolio_holdings`    |      322 |     322 |
| `10_benchmark_indices`     |     8050 |    8050 |

---

## 🧾 SQL Files

| File              | Description                              |
| ----------------- | ---------------------------------------- |
| `sql/schema.sql`  | SQLite schema and table creation queries |
| `sql/queries.sql` | Analytical SQL queries for reporting     |

The `queries.sql` file includes queries for:

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

# 📅 Task 1: Project Setup + Data Ingestion

## ✅ Completed

* Created project folder structure
* Initialized Git repository
* Installed required Python dependencies
* Created `requirements.txt`
* Loaded all 10 provided CSV datasets using Pandas
* Printed `.shape`, `.dtypes`, and `.head()` for each dataset
* Explored `fund_master` dataset
* Validated AMFI scheme codes between `fund_master` and `nav_history`
* Fetched live NAV data from MFAPI
* Saved live NAV data as raw CSV files
* Generated data quality summary reports

---

## 🌐 MFAPI Live NAV Fetch

Live NAV data was fetched from:

```text
https://api.mfapi.in/mf/{scheme_code}
```

### Scheme Code Validation Summary

| Assigned Fund       | Scheme Code | Validation Status |
| ------------------- | ----------: | ----------------- |
| HDFC Top 100 Direct |      125497 | Mismatch found    |
| SBI Bluechip        |      119551 | Mismatch found    |
| ICICI Bluechip      |      120503 | Mismatch found    |
| Nippon Large Cap    |      118632 | Matched           |
| Axis Bluechip       |      119092 | Mismatch found    |
| Kotak Bluechip      |      120841 | Mismatch found    |

Some assigned MFAPI scheme codes returned different scheme names than expected. These were recorded as data-quality anomalies.

---

# 📅 Task 2: Data Cleaning + SQLite Database Design

## ✅ Completed

* Cleaned all 10 mutual fund datasets
* Created cleaned CSV files in `data/processed/`
* Created SQLite database
* Loaded cleaned datasets into SQLite tables
* Verified row counts between CSV files and database tables
* Created `sql/schema.sql`
* Created `sql/queries.sql`
* Created `reports/data_dictionary.md`

---

# 📅 Task 3: Exploratory Data Analysis

## ✅ Completed

* Created EDA notebook: `notebooks/03_eda_analysis.ipynb`
* Loaded cleaned datasets from `data/processed/`
* Performed NAV trend analysis
* Created normalized NAV index chart
* Generated annual NAV return heatmap
* Analyzed AUM growth by fund house
* Analyzed SIP inflow trend
* Created category-wise net inflow heatmap
* Analyzed investor demographics
* Created state-wise SIP distribution chart
* Created T30 vs B30 city tier distribution chart
* Created folio count growth chart
* Computed NAV daily return correlation matrix
* Created sector allocation donut chart
* Created NAV volatility analysis
* Exported PNG and HTML charts

---

## 📊 EDA Charts Generated

All EDA charts are saved in:

```text
reports/charts/
```

Important chart outputs include:

| Chart File                             | Description               |
| -------------------------------------- | ------------------------- |
| `01_nav_trend_all_schemes.png`         | Daily NAV trend           |
| `02_normalized_nav_index.png`          | Normalized NAV comparison |
| `03_annual_nav_return_heatmap.png`     | Annual return heatmap     |
| `04_aum_growth_grouped_bar.png`        | AUM growth by fund house  |
| `05_aum_ranking_2025.png`              | AUM ranking               |
| `06_sip_inflow_timeseries.html`        | SIP inflow trend          |
| `08_category_inflow_heatmap.png`       | Category inflow heatmap   |
| `12_sip_amount_by_state.png`           | SIP amount by state       |
| `15_nav_return_correlation_matrix.png` | NAV return correlation    |
| `16_sector_allocation_donut.png`       | Sector allocation         |
| `17_nav_volatility_by_fund.png`        | NAV volatility            |

---

# 📅 Task 4: Fund Performance Analytics

## ✅ Completed

* Created performance notebook: `notebooks/04_performance_analytics.ipynb`
* Computed daily returns for all 40 schemes
* Calculated 1-year, 3-year, and 5-year CAGR
* Computed Sharpe Ratio using 6.5% risk-free rate
* Computed Sortino Ratio using downside deviation
* Calculated Alpha and Beta using Nifty 100 benchmark returns
* Computed R-squared values
* Calculated Maximum Drawdown
* Created fund scorecard
* Ranked all 40 funds using a weighted composite score
* Compared top 5 funds against Nifty 50 and Nifty 100
* Calculated tracking error
* Exported CSV files and charts

---

## 🧮 Key Performance Formulas

### Daily Returns

```text
daily_return = NAV_t / NAV_t-1 - 1
```

### CAGR

```text
CAGR = (NAV_end / NAV_start) ^ (1 / years) - 1
```

### Sharpe Ratio

```text
Sharpe Ratio = ((Average Daily Return - Daily Risk-Free Rate) / Standard Deviation) × √252
```

### Sortino Ratio

```text
Sortino Ratio = ((Average Daily Return - Daily Risk-Free Rate) / Downside Deviation) × √252
```

### Alpha and Beta

```text
Beta = Regression slope
Alpha = Regression intercept × 252
```

### Maximum Drawdown

```text
Drawdown = NAV / Running Maximum NAV - 1
```

### Tracking Error

```text
Tracking Error = Standard Deviation(Fund Return - Benchmark Return) × √252
```

---

## 📊 Performance Outputs

Files are saved in:

```text
reports/performance/
```

| File                      | Description                                 |
| ------------------------- | ------------------------------------------- |
| `alpha_beta.csv`          | Alpha, beta, and R-squared metrics          |
| `fund_scorecard.csv`      | Composite fund ranking                      |
| `performance_summary.csv` | CAGR, Sharpe, Sortino, and drawdown summary |
| `tracking_error_top5.csv` | Tracking error for top funds                |

---

## 🏆 Top 5 Funds by Composite Score

| Rank | Fund Name                                     |
| ---: | --------------------------------------------- |
|    1 | Kotak Flexicap Fund - Regular - Growth        |
|    2 | ICICI Pru Midcap Fund - Regular - Growth      |
|    3 | Mirae Asset Large Cap Fund - Regular - Growth |
|    4 | Axis Midcap Fund - Regular - Growth           |
|    5 | DSP Small Cap Fund - Regular - Growth         |

---

# 📅 Task 5: Advanced Analytics + Risk Metrics

## ✅ Completed

* Created advanced analytics notebook: `notebooks/05_advanced_analytics.ipynb`
* Computed daily returns for all 40 schemes
* Calculated Historical VaR 95%
* Calculated Conditional VaR 95%
* Generated `var_cvar_report.csv`
* Computed annualized volatility
* Created Rolling 90-day Sharpe Ratio analysis
* Saved rolling Sharpe chart
* Performed investor cohort analysis
* Performed SIP continuity analysis
* Built risk-based fund recommender
* Created `scripts/recommender.py`
* Calculated Sector HHI concentration
* Created advanced insights markdown file
* Exported advanced analytics CSV reports

---

## 📊 Advanced Analytics Outputs

Files are saved in:

```text
reports/advanced_analytics/
```

| File                           | Description                          |
| ------------------------------ | ------------------------------------ |
| `var_cvar_report.csv`          | VaR and CVaR report for all schemes  |
| `investor_cohort_analysis.csv` | Investor cohort analysis             |
| `sip_continuity_report.csv`    | SIP continuity and at-risk investors |
| `sector_hhi_concentration.csv` | Sector concentration using HHI       |
| `advanced_insights.md`         | Key advanced analytics findings      |

---

## 🧮 Advanced Risk Formulas

### Historical VaR 95%

```text
VaR 95% = 5th percentile of daily return distribution
```

### Conditional VaR 95%

```text
CVaR 95% = Mean of returns below VaR threshold
```

### Rolling 90-Day Sharpe Ratio

```text
Rolling Sharpe = returns.rolling(90).mean() / returns.rolling(90).std() × √252
```

### Sector HHI

```text
HHI = Σ(weight_i²)
```

Higher HHI indicates higher portfolio concentration.

---

## 🤖 Fund Recommender

The recommender suggests top funds based on investor risk appetite.

Run from project root:

```bash
python scripts/recommender.py --risk Low
python scripts/recommender.py --risk Moderate
python scripts/recommender.py --risk High
```

### Low Risk Recommendations

| Rank | Fund Name                                |
| ---: | ---------------------------------------- |
|    1 | ICICI Pru Liquid Fund - Regular - Growth |
|    2 | Kotak Liquid Fund - Regular - Growth     |
|    3 | ABSL Liquid Fund - Regular - Growth      |

### Moderate Risk Recommendations

| Rank | Fund Name                                      |
| ---: | ---------------------------------------------- |
|    1 | Mirae Asset Large Cap Fund - Regular - Growth  |
|    2 | SBI Bluechip Fund - Regular Plan - Growth      |
|    3 | Nippon India Large Cap Fund - Regular - Growth |

### High Risk Recommendations

| Rank | Fund Name                                |
| ---: | ---------------------------------------- |
|    1 | ICICI Pru Midcap Fund - Regular - Growth |
|    2 | DSP Midcap Fund - Regular - Growth       |
|    3 | Axis Midcap Fund - Regular - Growth      |

---

## 📈 Charts Generated

All charts are saved in:

```text
reports/charts/
```

Important chart files:

| Chart File                      | Description                           |
| ------------------------------- | ------------------------------------- |
| `benchmark_comparison_top5.png` | Top 5 funds vs Nifty 50 and Nifty 100 |
| `daily_return_distribution.png` | Daily return distribution             |
| `rolling_sharpe_chart.png`      | Rolling 90-day Sharpe Ratio           |

---

## 📊 Dashboard Status

Dashboard deliverable:

```text
dashboard/bluestock_mf.pbix
```

Dashboard pages planned:

1. Industry Overview
2. Fund Performance
3. Investor Insights
4. Risk & Advanced Analytics

Each dashboard page should include at least two slicers such as:

* Year
* Fund House
* Category
* Scheme Name
* Risk Level
* State
* Age Group

---

## 📄 Final Report and Presentation Status

Final report:

```text
reports/Final_Report.pdf
```

Presentation:

```text
reports/Presentation.pptx
```

Recommended report sections:

1. Project Title
2. Objective
3. Dataset Overview
4. ETL Pipeline
5. SQLite Database
6. EDA Insights
7. Performance Analytics
8. Advanced Analytics
9. Dashboard Screenshots
10. Key Findings
11. Conclusion

Recommended presentation slides:

1. Title
2. Objective
3. Dataset Overview
4. ETL Pipeline
5. EDA Insights
6. Performance Metrics
7. Advanced Analytics
8. Dashboard Preview
9. Key Findings
10. Thank You

---

## ⚠️ Important Repository Note

SQLite database files are excluded from GitHub using `.gitignore`.

```gitignore
*.db
data/db/*.db
__pycache__/
.ipynb_checkpoints/
venv/
.env
scripts/data/
scripts/reports/
```

The database file should be uploaded to Google Drive only:

```text
data/db/bluestock_mf.db
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

## ✅ Current Status

**Task 1 Completed**
**Task 2 Completed**
**Task 3 Completed**
**Task 4 Completed**
**Task 5 Completed**

Remaining final submission items:

* `dashboard/bluestock_mf.pbix`
* `reports/Final_Report.pdf`
* `reports/Presentation.pptx`

---
