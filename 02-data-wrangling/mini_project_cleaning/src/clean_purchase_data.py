import pandas as pd
from dateutil import parser

# ---------------------------
# Normalization dictionaries
# ---------------------------

# Fix spelling inconsistencies
CITY_NORMALIZATION = {
    "banglore": "Bangalore",
    "bengaluru": "Bangalore",
    "delhii": "Delhi"
}

# Convert text prices to numeric values
PRICE_TEXT_MAP = {
    "55k": 55000,
    "fifty thousand": 50000
}

# Convert text ages to numeric
AGE_TEXT_MAP = {
    "thirty four": 34
}

# ---------------------------
# Cleaning function
# ---------------------------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and normalizes extracted raw data.
    Performs validation, correction, and standardization.
    """

    # -------- Name --------
    # Capitalize names properly
    df["name"] = df["name_raw"].str.title()

    # -------- Age --------
    # Convert numeric strings to numbers
    df["age"] = pd.to_numeric(df["age_raw"], errors="coerce")

    # Remove invalid ages (<0 or >100)
    df.loc[(df["age"] < 0) | (df["age"] > 100), "age"] = None

    # -------- City --------
    # Normalize spelling then capitalize
    df["city"] = (
        df["city_raw"]
        .map(CITY_NORMALIZATION)
        .fillna(df["city_raw"])
        .str.title()
    )

    # -------- Product --------
    # Capitalize product names
    df["product"] = df["product_raw"].str.title()

    # -------- Price --------
    def normalize_price(val):
        """
        Converts raw price text into numeric value.
        """
        if pd.isna(val):
            return None

        # Clean symbols and formatting
        val = val.lower().replace("₹", "").replace(",", "").strip()

        # Handle text-based prices
        if val in PRICE_TEXT_MAP:
            return PRICE_TEXT_MAP[val]

        # Convert numeric strings
        return pd.to_numeric(val, errors="coerce")

    df["price"] = df["price_raw"].apply(normalize_price)

    # -------- Date --------
    def parse_date(val):
        """
        Safely parse multiple date formats.
        """
        if pd.isna(val):
            return None

        val = val.strip()

        try:
            # Prefer ISO formats (most reliable)
            if val[:4].isdigit() and ("-" in val or "/" in val):
                return pd.to_datetime(val, errors="coerce")

            # Fallback for flexible human formats
            return parser.parse(val, dayfirst=True)
        except:
            return None

    df["purchase_date"] = df["date_raw"].apply(parse_date)

    # -------- Final Output --------
    return df[
        ["name", "age", "city", "product", "price", "purchase_date"]
    ]


# ---------------------------
# Debug / Standalone execution
# ---------------------------

if __name__ == "__main__":
    from extract_purchase_entities import extract_entities
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent
    RAW_FILE = BASE_DIR / "data" / "raw" / "customer_purchase_events_dirty.txt"

    df_raw = extract_entities(RAW_FILE)
    df_clean = clean_data(df_raw)

    print(df_clean)
