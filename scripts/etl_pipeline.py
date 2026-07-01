from pathlib import Path
import subprocess
import sys
import os

BASE_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = BASE_DIR / "scripts"

steps = [
    "data_ingestion.py",
    "data_cleaning.py",
    "load_database.py",
]

def run_step(script_name):
    script_path = SCRIPTS_DIR / script_name

    if not script_path.exists():
        print(f"Missing script: {script_path}")
        return False

    print(f"\nRunning: {script_name}")

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=BASE_DIR,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        env=env
    )

    if result.stdout:
        print(result.stdout)

    if result.returncode != 0:
        print(f"Error in {script_name}")
        print(result.stderr)
        return False

    print(f"Completed: {script_name}")
    return True

def main():
    print("Bluestock Mutual Fund ETL Pipeline Started")

    for step in steps:
        success = run_step(step)
        if not success:
            print("ETL pipeline stopped due to error.")
            return

    print("\nETL pipeline completed successfully.")

if __name__ == "__main__":
    main()