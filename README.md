# 📊 Capstone Project I - Mutual Fund Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![ETL](https://img.shields.io/badge/ETL-Data%20Ingestion-orange)
![Status](https://img.shields.io/badge/Status-Day%201%20Completed-brightgreen)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)

## 🚀 Project Overview

This project is part of **Capstone Project I - Mutual Fund Analytics** for Bluestock Fintech.

The main objective of Task 1 is to set up the project structure, load mutual fund datasets, fetch live NAV data from MFAPI, validate AMFI scheme codes, and generate initial data quality reports.

---

## 📅 Task 1: Project Setup + Data Ingestion

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
* Committed and pushed Task 1 work to GitHub

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

## ▶️ Run Task 1 Scripts

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
git commit -m "Task 1: Data ingestion complete"
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

**Task 1 Completed Successfully**


---

# 📅 Task 2: Data Cleaning + SQLite Database Design

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
* Committed and pushed Task 2 work to GitHub

---

## 📁 Task 2 Updated Project Structure

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

## ▶️ Run Task 2 Scripts

Run data cleaning:

```bash
python data_cleaning.py
```

Load cleaned data into SQLite:

```bash
python load_database.py
```

---

## 🧾 Task 2 Git Commit

```bash
git add .
git commit -m "Task 2: Cleaned data + SQLite DB loaded"
git push
```

---

## ✅ Task 2 Status

Task 2 Completed Successfully.

---


---

# 📅 Task 3: Exploratory Data Analysis (EDA)

## ✅ Completed Tasks

* Created `EDA_Analysis.ipynb` notebook
* Loaded cleaned datasets from `data/processed/`
* Performed NAV trend analysis for mutual fund schemes from 2022–2026
* Highlighted 2023 bull run and 2024 market correction periods using Plotly
* Created normalized NAV index chart for better fund comparison
* Generated annual NAV return heatmap
* Created AUM growth grouped bar chart by fund house from 2022–2025
* Highlighted SBI Mutual Fund AUM dominance
* Created 2025 AUM ranking chart by fund house
* Analyzed monthly SIP inflow trend from Jan 2022 to Dec 2025
* Annotated Dec 2025 SIP all-time high of ₹31,002 Cr
* Created SIP 3-month rolling average trend chart
* Generated category-wise net inflow heatmap
* Analyzed investor age group distribution
* Created SIP amount box plot by age group
* Created investor gender split chart
* Analyzed geographic SIP distribution by state
* Created T30 vs B30 city tier distribution chart
* Created folio count growth chart from 13.26 Cr to 26.12 Cr
* Computed NAV daily return correlation matrix for 10 selected funds
* Created sector allocation donut chart from portfolio holdings data
* Created NAV volatility analysis by fund
* Created category inflow area trend chart
* Documented 10+ key EDA findings in Jupyter Markdown cells
* Exported 15+ charts as PNG files for final report usage
* Saved interactive Plotly charts as HTML files

---

## 📁 Task 3 Updated Project Structure

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
│   └── EDA_Analysis.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│
├── reports/
│   ├── charts/
│   │   ├── 01_nav_trend_all_schemes.png
│   │   ├── 02_normalized_nav_index.png
│   │   ├── 03_annual_nav_return_heatmap.png
│   │   ├── 04_aum_growth_grouped_bar.png
│   │   ├── 05_aum_ranking_2025.png
│   │   ├── 06_sip_inflow_timeseries.html
│   │   ├── 07_sip_rolling_average.png
│   │   ├── 08_category_inflow_heatmap.png
│   │   ├── 09_age_group_distribution_pie.png
│   │   ├── 10_sip_amount_boxplot_age_group.png
│   │   ├── 11_gender_split_bar.png
│   │   ├── 12_sip_amount_by_state.png
│   │   ├── 13_t30_b30_city_tier_pie.png
│   │   ├── 14_folio_count_growth.html
│   │   ├── 15_nav_return_correlation_matrix.png
│   │   ├── 16_sector_allocation_donut.png
│   │   ├── 17_nav_volatility_by_fund.png
│   │   └── 18_category_inflow_area_trend.png
│   │
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

## 📊 EDA Charts Generated

| No. | Chart Name                    | Description                                                 |
| --- | ----------------------------- | ----------------------------------------------------------- |
| 1   | Daily NAV Trend               | Shows NAV movement of mutual fund schemes from 2022–2026    |
| 2   | Normalized NAV Index          | Compares fund performance by indexing NAV values to 100     |
| 3   | Annual NAV Return Heatmap     | Shows yearly return performance by fund                     |
| 4   | AUM Growth Grouped Bar        | Compares fund-house AUM growth from 2022–2025               |
| 5   | 2025 AUM Ranking              | Ranks top fund houses by AUM in 2025                        |
| 6   | SIP Inflow Time Series        | Shows monthly SIP inflow trend with Dec 2025 ATH annotation |
| 7   | SIP Rolling Average           | Shows 3-month rolling average of SIP inflows                |
| 8   | Category Inflow Heatmap       | Shows category-wise net inflow intensity by month           |
| 9   | Age Group Distribution        | Shows investor age group distribution                       |
| 10  | SIP Amount Box Plot           | Compares SIP amount distribution across age groups          |
| 11  | Gender Split                  | Shows investor distribution by gender                       |
| 12  | SIP Amount by State           | Shows geographic SIP contribution by state                  |
| 13  | T30 vs B30 Pie Chart          | Shows investor distribution by city tier                    |
| 14  | Folio Count Growth            | Shows growth from 13.26 Cr to 26.12 Cr folios               |
| 15  | NAV Return Correlation Matrix | Shows pairwise return correlation between selected funds    |
| 16  | Sector Allocation Donut       | Shows aggregate sector allocation from portfolio holdings   |
| 17  | NAV Volatility by Fund        | Shows annualized NAV volatility by fund                     |
| 18  | Category Inflow Area Trend    | Shows category-wise inflow trend over time                  |

---

## 📈 Key EDA Findings

* NAV trends showed visible growth during the 2023 bull run and variation during 2024 correction periods.
* Normalized NAV index helped compare funds fairly despite different original NAV levels.
* Annual NAV return heatmap highlighted funds with stronger and weaker yearly performance.
* AUM analysis showed clear dominance of leading fund houses, especially SBI Mutual Fund.
* SIP inflows showed strong investor participation and reached an all-time high of ₹31,002 Cr in Dec 2025.
* Category inflow heatmap showed changing investor preference across fund categories.
* Investor demographics showed useful distribution patterns by age group and gender.
* SIP amount box plot helped compare investment behavior across age groups.
* Geographic analysis showed state-wise SIP participation and T30/B30 distribution.
* Folio count grew from 13.26 Cr in Jan 2022 to 26.12 Cr in Dec 2025.
* NAV return correlation matrix helped identify similarity between selected funds.
* Sector allocation donut chart showed major sector exposure across equity fund holdings.
* NAV volatility analysis identified funds with higher fluctuation risk.

---

## 📂 Exported Chart Files

All generated charts are saved in:

```text
reports/charts/
```

The folder contains PNG charts and interactive HTML files generated from Plotly visualizations.

---

## 🛠️ Tools and Libraries Used

| Tool / Library   | Purpose                                 |
| ---------------- | --------------------------------------- |
| Python           | Core programming language               |
| Pandas           | Data analysis and transformation        |
| NumPy            | Numerical calculations                  |
| Matplotlib       | Static chart generation                 |
| Seaborn          | Statistical visualizations and heatmaps |
| Plotly           | Interactive charts                      |
| Kaleido          | Plotly image export                     |
| Jupyter Notebook | EDA notebook development                |

---

## ▶️ Run Task 3 Notebook

Open Jupyter Notebook:

```bash
python -m notebook
```

Then open:

```text
notebooks/EDA_Analysis.ipynb
```

Run all notebook cells:

```text
Kernel → Restart Kernel and Run All Cells
```

---

## 📦 Task 3 Deliverables

| Deliverable               | Location                                   |
| ------------------------- | ------------------------------------------ |
| EDA Notebook              | `notebooks/EDA_Analysis.ipynb`             |
| Exported Charts           | `reports/charts/`                          |
| PNG Chart Files           | `reports/charts/*.png`                     |
| Interactive Plotly Charts | `reports/charts/*.html`                    |
| EDA Findings              | Markdown cells inside `EDA_Analysis.ipynb` |

---

## 🧾 Task 3 Git Commit

```bash
git add .
git commit -m "Task 3: Complete EDA analysis with exported charts"
git push
```

---

## ✅ Task 3 Status

Task 3 Completed Successfully.

---


# 📅 Task 4 : Fund Performance Analytics

## ✅ Completed Tasks

* Created `Performance_Analytics.ipynb` notebook
* Loaded cleaned NAV history from `data/processed/02_nav_history_clean.csv`
* Loaded fund master data from `data/processed/01_fund_master_clean.csv`
* Merged NAV data with fund master data using `amfi_code`
* Loaded benchmark index data from `data/processed/10_benchmark_indices_clean.csv`
* Converted benchmark data from long format into Nifty 50 and Nifty 100 columns
* Computed daily returns for all 40 mutual fund schemes
* Validated daily return distribution using histogram
* Calculated CAGR for 1-year, 3-year, and 5-year periods
* Computed Sharpe Ratio using 6.5% risk-free rate
* Computed Sortino Ratio using downside deviation
* Calculated Alpha and Beta using Nifty 100 benchmark returns
* Computed R-squared values for regression analysis
* Calculated Maximum Drawdown for each fund
* Identified worst drawdown start and end dates
* Created Fund Scorecard using weighted composite ranking
* Ranked all 40 funds on a 0–100 score scale
* Selected top 5 funds based on composite fund score
* Created benchmark comparison chart for top 5 funds vs Nifty 50 and Nifty 100
* Calculated tracking error against Nifty 50 and Nifty 100
* Exported performance CSV files and PNG charts for final submission

---

## 📁 Task 4 : Updated Project Structure

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
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│
├── reports/
│   ├── charts/
│   │   ├── benchmark_comparison_top5.png
│   │   └── daily_return_distribution.png
│   │
│   ├── performance/
│   │   ├── alpha_beta.csv
│   │   ├── fund_scorecard.csv
│   │   ├── performance_summary.csv
│   │   └── tracking_error_top5.csv
│   │
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

## 📊 Performance Metrics Implemented

| Metric           | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| Daily Returns    | Calculated day-to-day NAV percentage change for each scheme            |
| CAGR             | Computed 1-year, 3-year, and 5-year compounded annual growth rate      |
| Sharpe Ratio     | Measured risk-adjusted return using total volatility                   |
| Sortino Ratio    | Measured risk-adjusted return using downside volatility                |
| Alpha            | Calculated excess return over Nifty 100 benchmark using OLS regression |
| Beta             | Measured fund sensitivity against Nifty 100 benchmark returns          |
| R-squared        | Measured regression fit between fund returns and benchmark returns     |
| Maximum Drawdown | Identified largest peak-to-trough NAV decline                          |
| Tracking Error   | Measured deviation of fund returns from benchmark returns              |
| Fund Scorecard   | Ranked all funds using weighted composite scoring                      |

---

## 🧮 Key Formulas Used

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

Risk-free rate used:

```text
6.5%
```

### Sortino Ratio

```text
Sortino Ratio = ((Average Daily Return - Daily Risk-Free Rate) / Downside Deviation) × √252
```

### Alpha and Beta

Alpha and Beta were calculated using OLS regression against Nifty 100 daily returns.

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

## 🏆 Fund Scorecard Methodology

The final fund score was calculated on a 0–100 scale using weighted percentile ranks.

```text
Fund Score =
30% × 3-Year Return Rank
+ 25% × Sharpe Ratio Rank
+ 20% × Alpha Rank
+ 15% × Expense Ratio Rank Inverse
+ 10% × Maximum Drawdown Rank Inverse
```

Higher score indicates stronger overall performance based on return, risk-adjusted performance, alpha generation, cost efficiency, and drawdown control.

---

## 🔝 Top 5 Funds by Composite Score

| Rank | Fund Name                                     |
| ---- | --------------------------------------------- |
| 1    | Kotak Flexicap Fund - Regular - Growth        |
| 2    | ICICI Pru Midcap Fund - Regular - Growth      |
| 3    | Mirae Asset Large Cap Fund - Regular - Growth |
| 4    | Axis Midcap Fund - Regular - Growth           |
| 5    | DSP Small Cap Fund - Regular - Growth         |

---

## 📈 Task 4 :Charts Generated

| Chart File                      | Description                                                      |
| ------------------------------- | ---------------------------------------------------------------- |
| `benchmark_comparison_top5.png` | Compares top 5 funds against Nifty 50 and Nifty 100 over 3 years |
| `daily_return_distribution.png` | Shows daily return distribution across all mutual fund schemes   |

---

## 📦 Task 4 :Deliverables

| Deliverable                     | Location                                       |
| ------------------------------- | ---------------------------------------------- |
| Performance Analytics Notebook  | `notebooks/Performance_Analytics.ipynb`        |
| Fund Scorecard                  | `reports/performance/fund_scorecard.csv`       |
| Alpha and Beta Output           | `reports/performance/alpha_beta.csv`           |
| Tracking Error Output           | `reports/performance/tracking_error_top5.csv`  |
| Performance Summary             | `reports/performance/performance_summary.csv`  |
| Benchmark Comparison Chart      | `reports/charts/benchmark_comparison_top5.png` |
| Daily Return Distribution Chart | `reports/charts/daily_return_distribution.png` |

---

## 📌 Key Performance Findings

* All 40 mutual fund schemes were analyzed using historical NAV data.
* Daily return distribution was generated and validated for reasonableness.
* CAGR comparison helped identify funds with stronger long-term growth.
* Sharpe and Sortino ratios helped compare risk-adjusted fund performance.
* Alpha and Beta analysis measured performance relative to Nifty 100 benchmark.
* Maximum Drawdown analysis identified funds with higher downside risk.
* Composite scorecard ranked funds using return, risk, alpha, expense ratio, and drawdown metrics.
* Top 5 funds were compared against Nifty 50 and Nifty 100 using a normalized benchmark chart.
* Tracking error was calculated to measure fund deviation from benchmark returns.

---

## ⚠️ Data Note

The dataset appears to be academic/simulated and contains NAV values beyond the current date. All calculations were performed consistently for analytics, ranking, and comparison purposes.

---

## ▶️ Run Task 4 :Notebook

Open Jupyter Notebook:

```bash
python -m notebook
```

Then open:

```text
notebooks/Performance_Analytics.ipynb
```

Run all notebook cells:

```text
Kernel → Restart Kernel and Run All Cells
```

---

## 📦 Task 4 :Deliverables Summary

| Required File                   | Status    |
| ------------------------------- | --------- |
| `Performance_Analytics.ipynb`   | Completed |
| `fund_scorecard.csv`            | Completed |
| `alpha_beta.csv`                | Completed |
| `benchmark_comparison_top5.png` | Completed |
| `tracking_error_top5.csv`       | Completed |
| `performance_summary.csv`       | Completed |
| `daily_return_distribution.png` | Completed |

---

## 🧾 Task 4 :Git Commit

```bash
git add notebooks/Performance_Analytics.ipynb
git add reports/performance/alpha_beta.csv
git add reports/performance/fund_scorecard.csv
git add reports/performance/performance_summary.csv
git add reports/performance/tracking_error_top5.csv
git add reports/charts/benchmark_comparison_top5.png
git add reports/charts/daily_return_distribution.png
git add README.md
git commit -m "Day 4: Fund performance analytics complete"
git push
```

---

## ✅ Task 4 :Status
 Task 4 :Completed Successfully.

---
