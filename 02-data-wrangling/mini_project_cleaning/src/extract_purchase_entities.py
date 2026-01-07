# ---------------------------
# Standard library imports
# ---------------------------

import re                  # Used for regex-based pattern matching
import pandas as pd        # Used to create and manipulate DataFrames
from pathlib import Path   # OS-independent file path handling

# ---------------------------
# Path configuration
# ---------------------------

# Resolve the base project directory:
# .../02-data-wrangling/mini_project_cleaning
BASE_DIR = Path(__file__).resolve().parent.parent

# Full path to the raw unstructured text file
RAW_FILE = BASE_DIR / "data" / "raw" / "customer_purchase_events_dirty.txt"

# ---------------------------
# Reference vocabularies
# (Scalable – no hard coding per row)
# ---------------------------

# Known product keywords
PRODUCTS = [
    "iphone", "samsung tv", "laptop", "headphones",
    "washingmachine", "mobile", "ac", "refrigerator"
]

# Known city keywords (including misspellings)
CITIES = [
    "bangalore", "bengaluru", "banglore",
    "delhi", "delhii",
    "chennai", "mumbai", "kolkata", "pune"
]

# ---------------------------
# Entity Extraction Function
# ---------------------------

def extract_entities(input_file: Path) -> pd.DataFrame:
    """
    Reads raw unstructured text and extracts raw entities
    WITHOUT cleaning or validation.
    """

    records = []  # Will hold extracted rows as dictionaries

    # Open the raw text file safely
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Process each line independently
    for text in lines:

        # Convert to lowercase for consistent matching
        text_l = text.lower()

        # -------- Name Extraction --------
        # Looks for simple alphabetic names (3+ characters)
        name_match = re.search(
            r'(?:name:\s*)?([a-z]{3,})',
            text_l
        )

        # -------- Age Extraction --------
        # Captures numeric ages like "25", "-5", "32 yrs"
        age_match = re.search(
            r'age[:=]?\s*(-?\d+)|(\d+)\s*yrs',
            text_l
        )

        # -------- City Extraction --------
        # Finds the first city keyword present in text
        city_match = next(
            (c for c in CITIES if c in text_l),
            None
        )

        # -------- Product Extraction --------
        # Finds the first product keyword present
        product_match = next(
            (p for p in PRODUCTS if p in text_l),
            None
        )

        # -------- Price Extraction --------
        # Handles numeric, currency, "55k", and text prices
        price_match = re.search(
            r'₹?\s*\d{1,3},?\d{3}|\d+\s*k|fifty thousand',
            text_l
        )

        # -------- Date Extraction --------
        # Handles multiple real-world date formats
        date_match = re.search(
            r'\d{4}[-/]\d{2}[-/]\d{2}|'      # 2024-01-05
            r'\d{1,2}\s\w+\s\d{2,4}|'        # 10 Jan 24
            r'\w+\s\d{1,2}\s\d{4}',          # Jan 10 2024
            text_l
        )

        # Store raw extracted values (no cleaning here!)
        records.append({
            "name_raw": name_match.group(1) if name_match else None,
            "age_raw": age_match.group(1) if age_match else None,
            "city_raw": city_match,
            "product_raw": product_match,
            "price_raw": price_match.group() if price_match else None,
            "date_raw": date_match.group() if date_match else None
        })

    # Convert list of dicts into a structured DataFrame
    return pd.DataFrame(records)


# ---------------------------
# Standalone execution block
# ---------------------------

if __name__ == "__main__":
    # Run extraction independently for debugging
    df = extract_entities(RAW_FILE)
    print(df)
