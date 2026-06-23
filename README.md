# Capstone Project I - Mutual Fund Analytics

## Day 1: Project Setup + Data Ingestion

### Folder Structure

```text
mutual-fund-analytics/
├── data/
│   ├── raw/
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

### Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Run Day 1 Scripts

```bash
python data_ingestion.py
python live_nav_fetch.py
```

### Git Commands

```bash
git init
git add .
git commit -m "Day 1: Data ingestion complete"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mutual-fund-analytics.git
git push -u origin main
```

### Important Code Validation Note

The assignment mentions `125497` as HDFC Top 100 Direct. Validate this before submission because some sources/API results may show `125497` as a different scheme. The script saves `reports/live_nav_metadata.csv` so you can compare assigned fund name versus API returned scheme name.
