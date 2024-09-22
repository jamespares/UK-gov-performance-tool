# src/data_processing/pipeline.py

from src.data_processing.fetch_data import fetch_government_data, scrape_budget_report
from src.data_processing.clean_data import clean_budget_data, clean_staff_data
from src.data_processing.store_data import store_data

def run_data_pipeline():
    """
    Main function to run the data pipeline.
    Fetch data, clean it, and store it in the database.
    """
    # Fetch budget data from API
    budget_api_url = "https://api.gov.example/budget"
    budget_df = fetch_government_data(budget_api_url)
    
    # Clean the budget data
    cleaned_budget_df = clean_budget_data(budget_df)

    # Store the cleaned budget data in the database
    store_data(cleaned_budget_df, table_name="budget_data")

    # Fetch staffing data (scraping or another API)
    staffing_api_url = "https://api.gov.example/staffing"
    staffing_df = fetch_government_data(staffing_api_url)

    # Clean staffing data
    cleaned_staffing_df = clean_staff_data(staffing_df)

    # Store staffing data
    store_data(cleaned_staffing_df, table_name="staffing_data")

# Call this function from a CRON job or scheduler
if __name__ == "__main__":
    run_data_pipeline()
