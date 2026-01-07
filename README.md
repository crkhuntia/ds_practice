# Data Wrangling Mini Project – Unstructured to Structured Data

This README explains **step by step** what this project does, **why each step exists**, and **how a beginner can run, debug, and understand the pipeline end‑to‑end**.

You should be able to clone/pull this project, run each file independently, and clearly understand how raw unstructured data becomes a clean structured dataset.

---

## 1️⃣ What problem are we solving?

In real-world data science and data engineering projects, data rarely comes in clean tables.

Instead, data often looks like:

* Free‑text logs
* Human-written sentences
* Emails, messages, event logs
* Semi‑structured records

Example:

> `Name: rahul age=25 city banglore bought iphone price 55k on 2024-01-05`

This project demonstrates how to:

* Read **unstructured text**
* Extract meaningful information
* Clean incorrect / inconsistent values
* Produce a **structured CSV dataset** ready for analysis

---

## 2️⃣ Project folder structure

```
02-data-wrangling/
└── mini_project_cleaning/
    ├── data/
    │   ├── raw/
    │   │   └── customer_purchase_events_dirty.txt
    │   └── processed/
    │       └── customer_purchase_events_cleaned.csv
    │
    └── src/
        ├── extract_purchase_entities.py
        ├── clean_purchase_data.py
        └── build_purchase_dataset.py
```

### Why this structure?

| Folder           | Purpose                                           |
| ---------------- | ------------------------------------------------- |
| `data/raw`       | Original uncleaned input data (never modified)    |
| `data/processed` | Final clean structured outputs                    |
| `src`            | All Python logic (extraction, cleaning, pipeline) |

This mirrors **real industry projects**.

---

## 3️⃣ Raw data (`customer_purchase_events_dirty.txt`)

This file contains **intentionally messy data** to simulate real-world problems:

* Spelling mistakes (banglore, delhii)
* Invalid ages (-5, 200)
* Prices with symbols, commas, words
* Different date formats
* Missing fields

⚠️ Important rule:

> **Raw data is never edited manually**. All fixes happen in code.

---

## 4️⃣ Step 1: Entity Extraction

### File: `extract_purchase_entities.py`

### What this step does

* Reads raw text line by line
* Uses **regex and keyword matching**
* Extracts raw signals into columns
* Does **NOT clean or validate data**

This step answers:

> *“What information exists in the text?”*

### Why extraction is separate from cleaning

Separation of concerns:

* Extraction = capture signals
* Cleaning = fix correctness

This makes debugging and scaling much easier.

### How to run

From project root:

```
python .\02-data-wrangling\mini_project_cleaning\src\extract_purchase_entities.py
```

### Expected output

A DataFrame with columns:

* `name_raw`
* `age_raw`
* `city_raw`
* `product_raw`
* `price_raw`
* `date_raw`

Seeing `None`, wrong values, or strange formats here is **EXPECTED and GOOD**.

---

## 5️⃣ Step 2: Data Cleaning

### File: `clean_purchase_data.py`

### What this step does

* Normalizes spelling
* Converts text to numbers
* Removes invalid values
* Parses dates safely
* Produces analysis‑ready columns

This step answers:

> *“Can this data be trusted and analyzed?”*

### Cleaning rules implemented

| Field   | Cleaning logic                 |
| ------- | ------------------------------ |
| Name    | Capitalization                 |
| Age     | Remove <0 or >100              |
| City    | Fix spelling + standard case   |
| Product | Normalize casing               |
| Price   | Remove symbols, text → numeric |
| Date    | ISO-first safe parsing         |

### How to run

```
python .\02-data-wrangling\mini_project_cleaning\src\clean_purchase_data.py
```

### Expected output

A clean DataFrame with:

* Invalid values removed
* Numeric prices
* Correct dates

⚠️ Dates are tricky — the code intentionally prioritizes ISO formats to avoid silent corruption.

---

## 6️⃣ Step 3: Full Pipeline Execution

### File: `build_purchase_dataset.py`

### What this step does

This file **orchestrates the full pipeline**:

1. Extract raw entities
2. Clean extracted data
3. Save final CSV

This mirrors **production ETL pipelines**.

### How to run

```
python .\02-data-wrangling\mini_project_cleaning\src\build_purchase_dataset.py
```

### Output

A new file is created:

```
data/processed/customer_purchase_events_cleaned.csv
```

This file is:

* Fully structured
* Analysis-ready
* Suitable for ML / BI / dashboards

---

## 7️⃣ How to debug step by step (BEGINNER FRIENDLY)

Recommended debugging approach:

1️⃣ Run extraction alone

* Observe raw columns
* Check regex behavior

2️⃣ Run cleaning alone

* Print intermediate columns
* Comment out rules to see impact

3️⃣ Modify raw data

* Add new bad rows
* Observe pipeline behavior

4️⃣ Re-run pipeline

* Confirm outputs update automatically

This is how **real engineers debug data systems**.

---

## 8️⃣ Key concepts you learn from this project

* What **data wrangling** really means
* Why unstructured data is hard
* Regex-based extraction
* Validation vs normalization
* Date parsing pitfalls
* Scalable design (no hard-coded rows)
* Production-style folder structure

---

## 9️⃣ Interview-ready explanation

> “This project converts unstructured text into structured data using a two-step pipeline: extraction and cleaning. The design separates concerns, avoids hard-coding, and handles real-world data issues like invalid ages, inconsistent dates, and noisy text.”

---

## 🔟 What you can build next

* Unit tests for cleaning logic
* Logging instead of print
* Config-driven rules (YAML)
* PySpark version
* NLP-based extraction (spaCy)
* Data quality reports

---

## ✅ Final note

If you understand and can explain this project:

* You are **NOT a beginner anymore**
* You understand **real-world data science workflows**

This project is safe to put on your **resume or GitHub**.
