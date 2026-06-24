import sqlite3
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

PROCESSED_DIR = Path("data/processed")
DB_PATH = "bluestock_mf.db"
SCHEMA_PATH = "sql/schema.sql"

engine = create_engine(f"sqlite:///{DB_PATH}")


def run_schema():
    with sqlite3.connect(DB_PATH) as conn:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
            schema_sql = file.read()

        conn.executescript(schema_sql)
        conn.commit()

    print("Schema created successfully.")


def load_cleaned_csvs():
    for file_path in PROCESSED_DIR.glob("*_clean.csv"):
        table_name = file_path.stem.replace("_clean", "")

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {file_path.name} into table {table_name}: {len(df)} rows")


def verify_row_counts():
    with engine.connect() as conn:
        for file_path in PROCESSED_DIR.glob("*_clean.csv"):
            table_name = file_path.stem.replace("_clean", "")
            df = pd.read_csv(file_path)

            safe_table_name = f'"{table_name}"'

            db_count = pd.read_sql(
                f"SELECT COUNT(*) AS count FROM {safe_table_name}",
                conn
            )["count"][0]

            print(f"{table_name}: CSV rows = {len(df)}, DB rows = {db_count}")


if __name__ == "__main__":
    run_schema()
    load_cleaned_csvs()
    verify_row_counts()

    print("Database loading completed.")