"""
Simple Fund Recommender
Advanced Analytics + Risk Metrics

Usage:
    python recommender.py
    python recommender.py --risk Low
    python recommender.py --risk Moderate
    python recommender.py --risk High

Expected:
    Run Advanced_Analytics.ipynb first so this file exists:
    reports/advanced_analytics/var_cvar_report.csv
"""

from pathlib import Path
import argparse
import pandas as pd

def detect_project_root() -> Path:
    cwd = Path.cwd()
    if cwd.name.lower() in {"notebooks", "scripts"}:
        return cwd.parent
    return cwd

def normalize_risk(value: str) -> str:
    value = str(value).strip().title()
    mapping = {
        "Medium": "Moderate",
        "Medium Risk": "Moderate",
        "Moderate Risk": "Moderate",
        "Low Risk": "Low",
        "High Risk": "High",
    }
    return mapping.get(value, value)

def recommend_funds(risk_appetite: str, top_n: int = 3) -> pd.DataFrame:
    project_root = detect_project_root()
    report_path = project_root / "reports" / "advanced_analytics" / "var_cvar_report.csv"

    if not report_path.exists():
        raise FileNotFoundError(
            f"Missing {report_path}. Run Advanced_Analytics.ipynb first."
        )

    df = pd.read_csv(report_path)

    required = ["fund_display_name", "risk_grade", "sharpe_ratio", "var_95", "cvar_95"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing required columns in var_cvar_report.csv: {missing}")

    risk_appetite = normalize_risk(risk_appetite)
    if risk_appetite not in ["Low", "Moderate", "High"]:
        raise ValueError("Risk appetite must be Low, Moderate, or High.")

    df["risk_grade_clean"] = df["risk_grade"].apply(normalize_risk)
    filtered = df[df["risk_grade_clean"] == risk_appetite].copy()

    if filtered.empty:
        print(f"No exact {risk_appetite} risk-grade funds found. Showing top funds overall.")
        filtered = df.copy()

    filtered["sharpe_ratio"] = pd.to_numeric(filtered["sharpe_ratio"], errors="coerce")
    filtered = filtered.dropna(subset=["sharpe_ratio"])

    cols = [
        "fund_display_name",
        "risk_grade",
        "sharpe_ratio",
        "var_95",
        "cvar_95",
        "annualized_volatility",
        "observations",
    ]
    cols = [c for c in cols if c in filtered.columns]

    return filtered.sort_values("sharpe_ratio", ascending=False).head(top_n)[cols]

def main():
    parser = argparse.ArgumentParser(description="Top 3 fund recommender by risk appetite.")
    parser.add_argument(
        "--risk",
        choices=["Low", "Moderate", "High", "low", "moderate", "high"],
        help="Risk appetite: Low, Moderate, or High"
    )
    parser.add_argument("--top", type=int, default=3, help="Number of recommendations")
    args = parser.parse_args()

    risk = args.risk
    if not risk:
        risk = input("Enter risk appetite (Low / Moderate / High): ").strip()

    recommendations = recommend_funds(risk, args.top)

    print("\nRecommended Funds")
    print("=" * 80)
    print(recommendations.to_string(index=False))
    print("=" * 80)

if __name__ == "__main__":
    main()