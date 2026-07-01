"""
Day 1 - Data Ingestion for Mutual Fund Analytics

What this script does:
1. Creates required project folders.
2. Loads CSV files from data/raw using pandas.
3. Prints shape, dtypes, and first 5 rows for every CSV.
4. Records common anomalies: duplicate rows, missing values, empty columns.
5. Validates AMFI scheme codes if fund_master and nav_history CSVs are available.
6. Saves reports in reports/.

Run:
    python data_ingestion.py
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
SQL_DIR = BASE_DIR / "sql"
DASHBOARD_DIR = BASE_DIR / "dashboard"
REPORTS_DIR = BASE_DIR / "reports"

REQUIRED_DIRS = [RAW_DIR, PROCESSED_DIR, NOTEBOOKS_DIR, SQL_DIR, DASHBOARD_DIR, REPORTS_DIR]


def create_project_folders() -> None:
    """Create all required folders if missing."""
    for folder in REQUIRED_DIRS:
        folder.mkdir(parents=True, exist_ok=True)
    print("✅ Project folders checked/created.")


def read_csv_safely(file_path: Path) -> pd.DataFrame | None:
    """Read CSV with fallback encodings."""
    encodings = ["utf-8", "utf-8-sig", "latin1"]
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            continue
        except Exception as exc:
            print(f"❌ Error reading {file_path.name}: {exc}")
            return None
    print(f"❌ Could not decode {file_path.name} with common encodings.")
    return None


def inspect_csv_files() -> dict[str, pd.DataFrame]:
    """Load and inspect all CSV files in data/raw."""
    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if not csv_files:
        print("⚠️ No CSV files found in data/raw. Add the 10 provided datasets first.")
        return {}

    loaded_data: dict[str, pd.DataFrame] = {}
    summary_rows: list[dict[str, object]] = []

    for file_path in csv_files:
        print("\n" + "=" * 90)
        print(f"📄 File: {file_path.name}")

        df = read_csv_safely(file_path)
        if df is None:
            summary_rows.append({
                "file_name": file_path.name,
                "status": "failed_to_read",
                "rows": None,
                "columns": None,
                "duplicate_rows": None,
                "missing_values": None,
                "empty_columns": None,
                "anomaly_notes": "File could not be read",
            })
            continue

        loaded_data[file_path.name] = df

        print("\nShape:")
        print(df.shape)

        print("\nDtypes:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        duplicate_rows = int(df.duplicated().sum())
        missing_values = int(df.isna().sum().sum())
        empty_columns = [col for col in df.columns if df[col].isna().all()]

        anomaly_notes = []
        if duplicate_rows > 0:
            anomaly_notes.append(f"{duplicate_rows} duplicate rows")
        if missing_values > 0:
            anomaly_notes.append(f"{missing_values} missing values")
        if empty_columns:
            anomaly_notes.append(f"Empty columns: {', '.join(empty_columns)}")
        if not anomaly_notes:
            anomaly_notes.append("No major anomaly found in basic checks")

        summary_rows.append({
            "file_name": file_path.name,
            "status": "loaded",
            "rows": df.shape[0],
            "columns": df.shape[1],
            "duplicate_rows": duplicate_rows,
            "missing_values": missing_values,
            "empty_columns": ", ".join(empty_columns),
            "anomaly_notes": " | ".join(anomaly_notes),
        })

    summary_df = pd.DataFrame(summary_rows)
    summary_path = REPORTS_DIR / "data_ingestion_summary.csv"
    summary_df.to_csv(summary_path, index=False)
    print(f"\n✅ Data ingestion summary saved: {summary_path}")

    return loaded_data


def find_dataset(loaded_data: dict[str, pd.DataFrame], keyword: str) -> tuple[str, pd.DataFrame] | tuple[None, None]:
    """Find a loaded dataset by keyword in file name."""
    keyword = keyword.lower()
    for file_name, df in loaded_data.items():
        if keyword in file_name.lower():
            return file_name, df
    return None, None


def find_scheme_code_column(df: pd.DataFrame) -> str | None:
    """Try to identify scheme code column from common column names."""
    possible_names = [
        "scheme_code",
        "Scheme Code",
        "SCHEME_CODE",
        "code",
        "Code",
        "amfi_code",
        "AMFI Code",
        "schemeCode",
    ]
    normalized = {col.lower().strip().replace(" ", "_"): col for col in df.columns}

    for name in possible_names:
        key = name.lower().strip().replace(" ", "_")
        if key in normalized:
            return normalized[key]

    for col in df.columns:
        lower_col = col.lower()
        if "scheme" in lower_col and "code" in lower_col:
            return col
        if "amfi" in lower_col and "code" in lower_col:
            return col

    return None


def validate_scheme_codes(loaded_data: dict[str, pd.DataFrame]) -> None:
    """Validate scheme codes between fund_master and nav_history, if available."""
    fund_master_name, fund_master = find_dataset(loaded_data, "fund_master")
    nav_history_name, nav_history = find_dataset(loaded_data, "nav_history")

    if fund_master is None or nav_history is None:
        print("\n⚠️ Scheme-code validation skipped.")
        print("Reason: fund_master.csv and/or nav_history.csv not found in data/raw.")
        return

    fund_code_col = find_scheme_code_column(fund_master)
    nav_code_col = find_scheme_code_column(nav_history)

    if fund_code_col is None or nav_code_col is None:
        print("\n⚠️ Scheme-code validation skipped.")
        print("Reason: Could not detect scheme code column in fund_master or nav_history.")
        return

    fund_codes = set(fund_master[fund_code_col].dropna().astype(str).str.strip())
    nav_codes = set(nav_history[nav_code_col].dropna().astype(str).str.strip())

    missing_in_nav = sorted(fund_codes - nav_codes)
    extra_in_nav = sorted(nav_codes - fund_codes)

    report_lines = [
        "Day 1 Data Quality Summary",
        "==========================",
        f"fund_master file: {fund_master_name}",
        f"nav_history file: {nav_history_name}",
        f"fund_master scheme code column: {fund_code_col}",
        f"nav_history scheme code column: {nav_code_col}",
        f"Total unique fund_master codes: {len(fund_codes)}",
        f"Total unique nav_history codes: {len(nav_codes)}",
        f"Codes in fund_master missing from nav_history: {len(missing_in_nav)}",
        f"Codes in nav_history not present in fund_master: {len(extra_in_nav)}",
        "",
        "Missing in nav_history:",
        ", ".join(missing_in_nav[:100]) if missing_in_nav else "None",
        "",
        "Extra in nav_history:",
        ", ".join(extra_in_nav[:100]) if extra_in_nav else "None",
    ]

    report_path = REPORTS_DIR / "data_quality_summary.txt"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    validation_df = pd.DataFrame({
        "metric": [
            "fund_master_unique_codes",
            "nav_history_unique_codes",
            "missing_in_nav_history",
            "extra_in_nav_history",
        ],
        "value": [len(fund_codes), len(nav_codes), len(missing_in_nav), len(extra_in_nav)],
    })
    validation_df.to_csv(REPORTS_DIR / "scheme_code_validation.csv", index=False)

    print(f"\n✅ Scheme-code validation report saved: {report_path}")


def explore_fund_master(loaded_data: dict[str, pd.DataFrame]) -> None:
    """Print unique fund houses, categories, sub-categories, and risk grades if columns exist."""
    fund_master_name, fund_master = find_dataset(loaded_data, "fund_master")

    if fund_master is None:
        print("\n⚠️ fund_master dataset not found. Fund-master exploration skipped.")
        return

    print("\n" + "=" * 90)
    print(f"🔎 Exploring fund master: {fund_master_name}")

    targets = {
        "fund houses": ["fund_house", "Fund House", "AMC", "amc", "fundHouse"],
        "categories": ["category", "Scheme Category", "scheme_category", "schemeCategory"],
        "sub-categories": ["sub_category", "Sub Category", "subcategory", "scheme_sub_category"],
        "risk grades": ["risk_grade", "Risk Grade", "risk", "Riskometer", "riskometer"],
    }

    lower_map = {col.lower().strip().replace(" ", "_"): col for col in fund_master.columns}

    for label, possible_cols in targets.items():
        selected_col = None
        for col in possible_cols:
            key = col.lower().strip().replace(" ", "_")
            if key in lower_map:
                selected_col = lower_map[key]
                break

        if selected_col is None:
            print(f"\n{label.title()}: column not found")
            continue

        unique_values = sorted(fund_master[selected_col].dropna().astype(str).unique())
        print(f"\nUnique {label} ({len(unique_values)}):")
        print(unique_values[:50])


def main() -> None:
    create_project_folders()
    loaded_data = inspect_csv_files()
    explore_fund_master(loaded_data)
    validate_scheme_codes(loaded_data)
    print("\n✅ Day 1 data ingestion process completed.")


if __name__ == "__main__":
    main()
