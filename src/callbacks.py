# src/callbacks.py

from dash import Output, Input
import plotly.graph_objects as go
from src.data_processing.process_data import load_historical_data

def register_callbacks(app):
    @app.callback(
        Output('time-series-chart', 'figure'),
        [Input('department-dropdown', 'value')]
    )
    def update_time_series_chart(department):
        # Load historical data
        df = load_historical_data(department)

        # Create time series plot with multiple lines
        fig = go.Figure()

        # Plot budget over time
        fig.add_trace(go.Scatter(
            x=df['Year'], y=df['Budget_Million_GBP'],
            mode='lines+markers', name='Budget (Million GBP)',
            line=dict(color='blue')
        ))

        # Plot staffing levels over time
        fig.add_trace(go.Scatter(
            x=df['Year'], y=df['Staff_Count'],
            mode='lines+markers', name='Staff Count (FTE)',
            line=dict(color='green'),
            yaxis='y2'  # Plot on the second y-axis
        ))

        # Plot performance outcome (e.g., Percentage achieving grade 5 or above in Maths & English)
        fig.add_trace(go.Scatter(
            x=df['Year'], y=df['Percentage_Achieving_Grade_5_Maths_English'],
            mode='lines+markers', name='Percentage Achieving Grade 5 in Maths & English',
            line=dict(color='orange'),
            yaxis='y3'  # Plot on the third y-axis
        ))

        # Update layout for dual or triple y-axes
        fig.update_layout(
            title=f"Time Series Analysis: {department}",
            xaxis_title="Year",
            yaxis=dict(
                title="Budget (Million GBP)",
                titlefont=dict(color="blue"),
                tickfont=dict(color="blue")
            ),
            yaxis2=dict(
                title="Staff Count (FTE)",
                titlefont=dict(color="green"),
                tickfont=dict(color="green"),
                overlaying='y',
                side='right'
            ),
            yaxis3=dict(
                title="Performance Metric",
                titlefont=dict(color="orange"),
                tickfont=dict(color="orange"),
                anchor="free",
                overlaying='y',
                side='right',
                position=0.85  # Shift this axis slightly to the right
            )
        )

        return fig
