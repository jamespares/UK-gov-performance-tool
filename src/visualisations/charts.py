# src/visualizations/charts.py

import plotly.express as px

def create_budget_pie_chart(df):
    fig = px.pie(df, names='Category', values='Amount',
                 title='Budget Allocation')
    return fig

def create_staffing_trends_line_chart(df):
    fig = px.line(df, x='Year', y='Staff_Count',
                  title='Staffing Trends Over Years')
    return fig

def create_correlation_scatter_plot(df):
    fig = px.scatter(df, x='Budget_Million_GBP', y='Literacy_Rate',
                     trendline='ols',
                     title='Budget vs. Literacy Rate Correlation')
    return fig
