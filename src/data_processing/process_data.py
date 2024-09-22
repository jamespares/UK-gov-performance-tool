# src/data_processing/process_data.py

import pandas as pd

def load_historical_data(department):
    """
    Load historical budget, staffing, and performance data for time series analysis.
    Currently using sample data, including staffing numbers for Department for Education.
    """
    if department == 'education':
        data = {
            'Year': [2012, 2016, 2020, 2023],  # Use the years where we have staffing data
            'Budget_Million_GBP': [75000, 80000, 85000, 87943],  # Historical budget data
            'Staff_Count': [3885, 2301, 2301, None],  # Staffing levels (in FTE) for given years
            'Percentage_Achieving_Grade_5_Maths_English': [43.0, 44.0, 45.0, 45.3],  # Performance data
            'Progress_8': [0.02, 0.03, 0.04, 0.05],  # Progress 8 over the years
            'Attainment_8': [45.0, 45.5, 46.0, 46.7]  # Attainment 8 over the years
        }
    else:
        # Placeholder for other departments
        data = {
            'Year': [2012, 2016, 2020, 2023],
            'Budget_Million_GBP': [0, 0, 0, 0],
            'Staff_Count': [0, 0, 0, 0],
            'Performance_Metric_1': [0, 0, 0, 0]
        }

    df = pd.DataFrame(data)
    return df
