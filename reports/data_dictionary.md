\# Data Dictionary



\## Project Name

Mutual Fund Analytics - Data Cleaning + SQLite Database Design



\## Database

bluestock\_mf.db



\## Processed Data Folder

data/processed/



\---



\## Tables Loaded into SQLite



| Table Name | Rows |

|---|---:|

| 01\_fund\_master | 40 |

| 02\_nav\_history | 46000 |

| 03\_aum\_by\_fund\_house | 90 |

| 04\_monthly\_sip\_inflows | 48 |

| 05\_category\_inflows | 144 |

| 06\_industry\_folio\_count | 21 |

| 07\_scheme\_performance | 40 |

| 08\_investor\_transactions | 32778 |

| 09\_portfolio\_holdings | 322 |

| 10\_benchmark\_indices | 8050 |



\---



\## 01\_fund\_master

Contains master information about mutual fund schemes.



\## 02\_nav\_history

Contains historical NAV data.



Cleaning:

\- Dates converted to datetime

\- Sorted by AMFI code and date

\- Missing NAV values forward-filled

\- Duplicates removed

\- NAV values less than or equal to 0 removed



\## 03\_aum\_by\_fund\_house

Contains AUM data grouped by fund house.



\## 04\_monthly\_sip\_inflows

Contains monthly SIP inflow data.



\## 05\_category\_inflows

Contains category-wise mutual fund inflows.



\## 06\_industry\_folio\_count

Contains folio count data.



\## 07\_scheme\_performance

Contains return and expense ratio details.



Cleaning:

\- Return values converted to numeric

\- Expense ratio validated between 0.1% and 2.5%

\- Anomalies flagged

\- Duplicates removed



\## 08\_investor\_transactions

Contains investor transaction details.



Cleaning:

\- Transaction type standardized

\- Amount validated greater than 0

\- Date formats fixed

\- KYC status values checked

\- Duplicates removed



\## 09\_portfolio\_holdings

Contains fund portfolio holdings data.



\## 10\_benchmark\_indices

Contains benchmark index historical data.



\---



\## Final Deliverables

\- 10 cleaned CSV files in data/processed/

\- bluestock\_mf.db

\- sql/schema.sql

\- sql/queries.sql

\- reports/data\_dictionary.md

