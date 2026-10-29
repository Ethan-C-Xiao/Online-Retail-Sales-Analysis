from pathlib import Path

import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_FILE = BASE_DIR / "data" / "raw" / "Online Retail.xlsx"
CLEAN_FILE = BASE_DIR / "data" / "cleaned" / "online_retail_cleaned.csv"
DATABASE_FILE = BASE_DIR / "database" / "online_retail.db"

df = pd.read_excel(RAW_FILE, engine = "openpyxl")

print("\n--- FIRST FIVE ROWS ---")
print(df.head()) 

print("\n--- NUMBER OF ROWS AND COLUMNS ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns)

print("\n--- DATA TYPES / INFO ---")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isna().sum())

print("\n--- DUPLICATES ---")
print(df.duplicated().sum())

print("\n--- DUPLICATE ROWS ---")
print(df[df.duplicated(keep = False)].head(10))

print("\n--- NON-POSITIVE QUANTITIES ---")
print((df["Quantity"] <= 0).sum())

print("\n--- NON-POSITIVE PRICES ---")
print((df["UnitPrice"] <= 0).sum())

print("\n--- CANCELLED INVOICES ---")
print(df["InvoiceNo"].astype(str).str.startswith("C").sum())

print("\n--- SAMPLE CANCELLED INVOICES ---")
print(
    df[df["InvoiceNo"].astype(str).str.startswith("C")].head(10)
)

print("\n--- ZERO PRICES ---")
print((df["UnitPrice"] == 0).sum())

print("\n--- NEGATIVE PRICES")
print((df["UnitPrice"] < 0).sum())

print("\n--- SAMPLE NON-POSITIVE PRICES ---")
print(df[df["UnitPrice"] <= 0].head(10))
