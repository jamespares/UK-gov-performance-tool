# src/callbacks.py

from dash import Output, Input
import pandas as pd
import plotly.express as px
from src.data_processing.process_data import load_budget_data, load_staffing_data, load_performance_metrics

def register_callbacks(app):
    @app.callback(
        [Output('budget-allocation-chart', 'figure'),
         Output('staffing-trends-chart', 'figure'),
         Output('output-outcome-correlation-chart', 'figure')],
        [Input('department-dropdown', 'value')]
    )
    def update_charts(department):
        # Load and process data based on department
        budget_df = load_budget_data(department)
        staffing_df = load_staffing_data(department)
        performance_df = load_performance_metrics(department)

        # Budget Allocation Pie Chart
        budget_fig = px.pie(budget_df, names='Category', values='Amount',
                            title='Budget Allocation')

        # Staffing Trends Line Graph
        staffing_fig = px.line(staffing_df, x='Year', y='Staff_Count',
                               title='Staffing Trends Over Years')

        # Output-Outcome Correlation Scatter Plot
        correlation_fig = px.scatter(performance_df, x='Budget_Million_GBP', y='Literacy_Rate',
                                     trendline='ols',
                                     title='Budget vs. Literacy Rate Correlation')

        return budget_fig, staffing_fig, correlation_fig
