import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_nav_history():
    file_path = RAW_DIR / "nav_history.csv"

    if not file_path.exists():
        print("nav_history.csv not found")
        return

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.lower().str.strip()

    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
    df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

    df = df.dropna(subset=["amfi_code", "date"])
    df = df.sort_values(["amfi_code", "date"])

    df["nav"] = df.groupby("amfi_code")["nav"].ffill()

    df = df.drop_duplicates()
    df = df[df["nav"] > 0]

    df.to_csv(PROCESSED_DIR / "nav_history_clean.csv", index=False)
    print("nav_history cleaned:", df.shape)


def clean_investor_transactions():
    file_path = RAW_DIR / "investor_transactions.csv"

    if not file_path.exists():
        print("investor_transactions.csv not found")
        return

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.lower().str.strip()

    if "transaction_date" in df.columns:
        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"],
            errors="coerce",
            dayfirst=True
        )

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    transaction_mapping = {
        "sip": "SIP",
        "s.i.p": "SIP",
        "lumpsum": "Lumpsum",
        "lump sum": "Lumpsum",
        "lump_sum": "Lumpsum",
        "redemption": "Redemption",
        "redeem": "Redemption",
        "withdrawal": "Redemption"
    }

    df["transaction_type"] = (
        df["transaction_type"]
        .astype(str)
        .str.lower()
        .str.strip()
        .replace(transaction_mapping)
    )

    valid_transaction_types = ["SIP", "Lumpsum", "Redemption"]
    df = df[df["transaction_type"].isin(valid_transaction_types)]

    df = df[df["amount"] > 0]

    if "kyc_status" in df.columns:
        df["kyc_status"] = df["kyc_status"].astype(str).str.title().str.strip()

        valid_kyc = ["Verified", "Pending", "Rejected"]
        df["kyc_status"] = df["kyc_status"].where(
            df["kyc_status"].isin(valid_kyc),
            "Pending"
        )

    df = df.drop_duplicates()

    df.to_csv(PROCESSED_DIR / "investor_transactions_clean.csv", index=False)
    print("investor_transactions cleaned:", df.shape)


def clean_scheme_performance():
    file_path = RAW_DIR / "scheme_performance.csv"

    if not file_path.exists():
        print("scheme_performance.csv not found")
        return

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.lower().str.strip()

    possible_return_cols = [
        "one_year_return",
        "three_year_return",
        "five_year_return",
        "1y_return",
        "3y_return",
        "5y_return"
    ]

    for col in possible_return_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("%", "", regex=False)
                .str.strip()
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "expense_ratio" in df.columns:
        df["expense_ratio"] = (
            df["expense_ratio"]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.strip()
        )
        df["expense_ratio"] = pd.to_numeric(df["expense_ratio"], errors="coerce")

        df["expense_ratio_status"] = df["expense_ratio"].apply(
            lambda x: "Valid" if pd.notna(x) and 0.1 <= x <= 2.5 else "Invalid"
        )

    return_cols = [col for col in possible_return_cols if col in df.columns]

    for col in return_cols:
        df[f"{col}_anomaly_flag"] = df[col].apply(
            lambda x: "Anomaly" if pd.notna(x) and (x > 100 or x < -100) else "Normal"
        )

    df = df.drop_duplicates()

    df.to_csv(PROCESSED_DIR / "scheme_performance_clean.csv", index=False)
    print("scheme_performance cleaned:", df.shape)


def copy_other_csvs():
    important_files = {
        "nav_history.csv",
        "investor_transactions.csv",
        "scheme_performance.csv"
    }

    for file_path in RAW_DIR.glob("*.csv"):
        if file_path.name not in important_files:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.lower().str.strip()
            df = df.drop_duplicates()

            output_name = file_path.stem + "_clean.csv"
            df.to_csv(PROCESSED_DIR / output_name, index=False)

            print(output_name, "created:", df.shape)


if __name__ == "__main__":
    clean_nav_history()
    clean_investor_transactions()
    clean_scheme_performance()
    copy_other_csvs()

    print("All cleaning completed.")