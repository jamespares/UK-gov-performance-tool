# src/data_processing/clean_data.py

def clean_budget_data(df):
    """
    Clean and normalize the budget data.
    - Normalize column names
    - Convert budget to millions (if required)
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_')  # Normalize column names
    df['budget_million_gbp'] = df['budget'] / 1_000_000  # Convert budget to millions
    return df

def clean_staff_data(df):
    """
    Clean and standardize staffing data.
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df
