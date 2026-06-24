DROP TABLE IF EXISTS fact_aum;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_fund;

CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE,
    fund_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    investor_id TEXT,
    transaction_date DATE,
    transaction_type TEXT,
    amount REAL,
    state TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    one_year_return REAL,
    three_year_return REAL,
    five_year_return REAL,
    expense_ratio REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    aum_date DATE,
    aum REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);