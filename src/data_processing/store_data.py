# src/data_processing/store_data.py

from sqlalchemy import create_engine

def store_data(df, table_name):
    """
    Store the cleaned data in a PostgreSQL database.
    """
    engine = create_engine('postgresql://user:password@localhost:5432/gov_data')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_data(table_name):
    """
    Load data from the database for visualization.
    """
    engine = create_engine('postgresql://user:password@localhost:5432/gov_data')
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, con=engine)
    return df
