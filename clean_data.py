from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

RAW_FILE = BASE_DIR / "data" / "raw" / "Online Retail.xlsx"
CLEAN_FILE = BASE_DIR / "data" / "cleaned" / "online_retail_cleaned.csv"

df = pd.read_excel(RAW_FILE, engine="openpyxl")

df.columns = (
    df.columns
    .str.strip()
    .str.replace(r"([a-z0-9])([A-Z])" , r"\1_\2", regex = True)
    .str.lower()
    .str.replace(r"[^a-z0-9]+" , "_", regex = True)
    .str.strip("_")
)

rows_before = len(df)

df = df.drop_duplicates()

rows_after = len(df)

print("\n--- TOTAL DUPLICATES REMOVED ---")
print(rows_before - rows_after)

#handle missing details
df["description"] = df["description"].fillna("Unknown")

#Convert customer IDs to nullable integers
df["customer_id"] = df["customer_id"].astype("Int64")

#isna means whether values are missing
print("\n--- MISSING VALUES AFTER CLEANING ---")
print(df.isna().sum())

df["invoice_date"] = pd.to_datetime(df["invoice_date"], errors="coerce")

df["invoice_no"] = df["invoice_no"].astype(str)
df["stock_code"] = df["stock_code"].astype(str)

print("\n--- DATA TYPES AFTER CLEANING ---")
print(df.dtypes)

print(df.columns.tolist())