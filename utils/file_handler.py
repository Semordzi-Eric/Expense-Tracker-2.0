import pandas as pd
from datetime import datetime
from utils.categorizer import auto_categorize

def process_csv_upload(file) -> pd.DataFrame:
    """
    Reads a CSV file, auto-detects common columns for a bank/momo statement,
    cleans the data, and auto-categorizes transactions.
    """
    # Try reading the file (could be comma or semicolon separated)
    try:
        df = pd.read_csv(file)
    except Exception as e:
        df = pd.read_csv(file, sep=';')
        
    # Standardize column names
    df.columns = df.columns.astype(str).str.lower().str.strip().str.replace(' ', '_')
    
    # Look for expected columns
    date_cols = [c for c in df.columns if 'date' in c or 'time' in c]
    amount_cols = [c for c in df.columns if 'amount' in c or 'value' in c or 'price' in c]
    desc_cols = [c for c in df.columns if 'desc' in c or 'detail' in c or 'narration' in c or 'ref' in c]
    
    if not date_cols or not amount_cols:
        raise ValueError("Could not auto-detect 'date' and 'amount' columns in the uploaded CSV.")
        
    date_col = date_cols[0]
    amount_col = amount_cols[0]
    desc_col = desc_cols[0] if desc_cols else None
    
    # Create standardized dataframe
    standard_df = pd.DataFrame()
    
    # Clean datetime
    try:
        standard_df['date'] = pd.to_datetime(df[date_col]).dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        # Fallback if parsing fails
        standard_df['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    # Clean amount
    # Remove currency symbols and commas
    amounts = df[amount_col].astype(str).str.replace(r'[^\d.-]', '', regex=True)
    standard_df['amount'] = pd.to_numeric(amounts, errors='coerce').fillna(0)
    
    # Description
    if desc_col:
        standard_df['description'] = df[desc_col].astype(str).fillna('CSV Import')
    else:
        standard_df['description'] = 'CSV Import'
        
    # Auto-categorize
    standard_df['category'] = standard_df['description'].apply(auto_categorize)
    standard_df['payment_method'] = 'import'
    standard_df['subcategory'] = ''
    standard_df['tags'] = 'csv'
    
    return standard_df
