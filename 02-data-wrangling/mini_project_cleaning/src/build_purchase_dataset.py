from pathlib import Path

# Import pipeline steps
from extract_purchase_entities import extract_entities
from clean_purchase_data import clean_data

# ---------------------------
# Path configuration
# ---------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "customer_purchase_events_dirty.txt"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "customer_purchase_events_cleaned.csv"

# ---------------------------
# Pipeline orchestration
# ---------------------------

def main():
    """
    Executes the full data wrangling pipeline:
    raw text → extracted → cleaned → CSV
    """

    # Step 1: Extract raw entities
    df_raw = extract_entities(RAW_FILE)

    # Step 2: Clean and normalize
    df_clean = clean_data(df_raw)

    # Step 3: Save final structured dataset
    df_clean.to_csv(OUTPUT_FILE, index=False)

    print("✅ Pipeline executed successfully")
    print(f"📁 Output saved to: {OUTPUT_FILE}")

# ---------------------------
# Entry point
# ---------------------------

if __name__ == "__main__":
    main()
