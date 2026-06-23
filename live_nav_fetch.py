"""
Day 1 - Live NAV Fetch from MFAPI

What this script does:
1. Fetches NAV history from MFAPI for selected scheme codes.
2. Saves each scheme as a raw CSV in data/raw/live_nav/.
3. Saves one combined CSV in data/raw/live_nav/all_live_nav_history.csv.
4. Saves API metadata separately for validation.

Run:
    python live_nav_fetch.py
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import time
import requests
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_NAV_DIR = BASE_DIR / "data" / "raw" / "live_nav"
REPORTS_DIR = BASE_DIR / "reports"
RAW_NAV_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

MFAPI_BASE_URL = "https://api.mfapi.in/mf"

# Use the codes assigned in your task, but validate scheme_name from API output.
# Important: 125497 may not be HDFC Top 100 in every source/API response.
SCHEMES = {
    "HDFC Top 100 Direct - assigned code, verify": 125497,
    "SBI Bluechip / SBI Large Cap Direct": 119551,
    "ICICI Prudential Bluechip Direct": 120503,
    "Nippon India Large Cap Direct": 118632,
    "Axis Bluechip Direct": 119092,
    "Kotak Bluechip Direct": 120841,
}


def fetch_nav_history(scheme_code: int) -> dict:
    """Fetch full NAV history for one scheme code."""
    url = f"{MFAPI_BASE_URL}/{scheme_code}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def parse_nav_response(payload: dict, assigned_name: str, scheme_code: int) -> tuple[pd.DataFrame, dict]:
    """Convert MFAPI payload into dataframe and metadata."""
    meta = payload.get("meta", {}) or {}
    data = payload.get("data", []) or []

    nav_df = pd.DataFrame(data)
    if not nav_df.empty:
        nav_df["scheme_code"] = scheme_code
        nav_df["assigned_name"] = assigned_name
        nav_df["api_scheme_name"] = meta.get("scheme_name")
        nav_df["fund_house"] = meta.get("fund_house")
        nav_df["scheme_category"] = meta.get("scheme_category")
        nav_df["fetched_at"] = datetime.now().isoformat(timespec="seconds")

        if "date" in nav_df.columns:
            nav_df["date"] = pd.to_datetime(nav_df["date"], format="%d-%m-%Y", errors="coerce")
        if "nav" in nav_df.columns:
            nav_df["nav"] = pd.to_numeric(nav_df["nav"], errors="coerce")

    metadata = {
        "assigned_name": assigned_name,
        "requested_scheme_code": scheme_code,
        "api_scheme_code": meta.get("scheme_code"),
        "api_scheme_name": meta.get("scheme_name"),
        "fund_house": meta.get("fund_house"),
        "scheme_type": meta.get("scheme_type"),
        "scheme_category": meta.get("scheme_category"),
        "isin_growth": meta.get("isin_growth"),
        "isin_div_reinvestment": meta.get("isin_div_reinvestment"),
        "records_fetched": len(nav_df),
        "latest_date": str(nav_df["date"].max().date()) if not nav_df.empty and "date" in nav_df.columns and nav_df["date"].notna().any() else None,
        "latest_nav": float(nav_df.sort_values("date")["nav"].iloc[-1]) if not nav_df.empty and "nav" in nav_df.columns else None,
        "fetched_at": datetime.now().isoformat(timespec="seconds"),
    }
    return nav_df, metadata


def safe_file_name(name: str, scheme_code: int) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "_" for ch in name)
    cleaned = "_".join(part for part in cleaned.split("_") if part)
    return f"{scheme_code}_{cleaned[:70]}.csv"


def main() -> None:
    all_nav_frames: list[pd.DataFrame] = []
    metadata_rows: list[dict] = []
    failed_rows: list[dict] = []

    for assigned_name, scheme_code in SCHEMES.items():
        print(f"\nFetching {assigned_name} ({scheme_code})...")
        try:
            payload = fetch_nav_history(scheme_code)
            nav_df, metadata = parse_nav_response(payload, assigned_name, scheme_code)

            output_file = RAW_NAV_DIR / safe_file_name(assigned_name, scheme_code)
            nav_df.to_csv(output_file, index=False)

            all_nav_frames.append(nav_df)
            metadata_rows.append(metadata)

            print(f"✅ Saved: {output_file}")
            print(f"API scheme name: {metadata.get('api_scheme_name')}")
            print(f"Records: {metadata.get('records_fetched')}")

            # Gentle pause to avoid rapid repeated requests.
            time.sleep(0.5)

        except Exception as exc:
            print(f"❌ Failed for {assigned_name} ({scheme_code}): {exc}")
            failed_rows.append({
                "assigned_name": assigned_name,
                "scheme_code": scheme_code,
                "error": str(exc),
                "fetched_at": datetime.now().isoformat(timespec="seconds"),
            })

    if all_nav_frames:
        combined_df = pd.concat(all_nav_frames, ignore_index=True)
        combined_path = RAW_NAV_DIR / "all_live_nav_history.csv"
        combined_df.to_csv(combined_path, index=False)
        print(f"\n✅ Combined NAV history saved: {combined_path}")

    metadata_df = pd.DataFrame(metadata_rows)
    metadata_path = REPORTS_DIR / "live_nav_metadata.csv"
    metadata_df.to_csv(metadata_path, index=False)
    print(f"✅ Metadata saved: {metadata_path}")

    if failed_rows:
        failed_df = pd.DataFrame(failed_rows)
        failed_path = REPORTS_DIR / "live_nav_failed_requests.csv"
        failed_df.to_csv(failed_path, index=False)
        print(f"⚠️ Failed request report saved: {failed_path}")

    print("\n✅ Live NAV fetch completed.")


if __name__ == "__main__":
    main()
