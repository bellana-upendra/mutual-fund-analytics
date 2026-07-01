from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
PERFORMANCE_DIR = BASE_DIR / "reports" / "performance"
ADVANCED_DIR = BASE_DIR / "reports" / "advanced_analytics"

def main():
    print("Bluestock Mutual Fund Metrics Check")
    print("-" * 50)

    if PERFORMANCE_DIR.exists():
        print(f"✅ Performance folder found: {PERFORMANCE_DIR}")
        for file in PERFORMANCE_DIR.glob("*"):
            print(f"   - {file.name}")
    else:
        print("⚠️ Performance folder not found.")

    if ADVANCED_DIR.exists():
        print(f"\n✅ Advanced analytics folder found: {ADVANCED_DIR}")
        for file in ADVANCED_DIR.glob("*"):
            print(f"   - {file.name}")
    else:
        print("⚠️ Advanced analytics folder not found.")

    print("\n✅ Metrics output check completed.")

if __name__ == "__main__":
    main()