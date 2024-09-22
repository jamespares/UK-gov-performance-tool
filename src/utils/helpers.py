# src/utils/helpers.py

def calculate_correlation(x, y):
    from scipy.stats import pearsonr
    corr, _ = pearsonr(x, y)
    return corr

def preprocess_data(df):
    # Placeholder for data preprocessing steps
    # e.g., handling missing values, normalizing data
    df_clean = df.dropna()
    return df_clean
