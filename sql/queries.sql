-- 1. View fund master data
SELECT *
FROM "01_fund_master"
LIMIT 10;


-- 2. Average NAV per month
SELECT 
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM "02_nav_history"
GROUP BY strftime('%Y-%m', date)
ORDER BY month;


-- 3. Highest NAV funds
SELECT 
    amfi_code,
    date,
    nav
FROM "02_nav_history"
ORDER BY nav DESC
LIMIT 10;


-- 4. Top fund houses by AUM
SELECT *
FROM "03_aum_by_fund_house"
LIMIT 10;


-- 5. Monthly SIP inflow trend
SELECT *
FROM "04_monthly_sip_inflows"
ORDER BY 1;


-- 6. Category-wise inflows
SELECT *
FROM "05_category_inflows"
LIMIT 20;


-- 7. Industry folio count summary
SELECT *
FROM "06_industry_folio_count"
LIMIT 20;


-- 8. Funds with expense ratio less than 1%
SELECT *
FROM "07_scheme_performance"
WHERE expense_ratio < 1;


-- 9. Transactions by state
SELECT 
    state,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_transactions DESC;


-- 10. Transaction type summary
SELECT 
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM "08_investor_transactions"
GROUP BY transaction_type
ORDER BY total_amount DESC;