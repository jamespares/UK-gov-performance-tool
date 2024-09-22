# src/visualizations.py

import plotly.express as px
from src.data_processing.store_data import load_data

def generate_budget_plot(department):
    """
    Generate a budget time series plot for a given department.
    """
    df = load_data('budget_data')  # Load budget data from database
    filtered_df = df[df['department'] == department]

    fig = px.line(filtered_df, x='year', y='budget_million_gbp', title=f'{department} Budget Over Time')
    return fig

def generate_staffing_plot(department):
    """
    Generate a staffing levels plot for a given department.
    """
    df = load_data('staffing_data')  # Load staffing data from database
    filtered_df = df[df['department'] == department]

    fig = px.line(filtered_df, x='year', y='staff_count', title=f'{department} Staffing Levels Over Time')
    return fig
