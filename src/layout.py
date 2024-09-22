# src/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

def layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Government Performance Dashboard"), width=12)
        ]),
        dbc.Row([
            dbc.Col([
                html.Label("Select Department"),
                dcc.Dropdown(
                    id='department-dropdown',
                    options=[
                        {'label': 'Department for Education', 'value': 'education'},
                        # Add more departments as needed
                    ],
                    value='education',
                    clearable=False
                )
            ], width=4),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='budget-allocation-chart')
            ], width=6),
            dbc.Col([
                dcc.Graph(id='staffing-trends-chart')
            ], width=6),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='output-outcome-correlation-chart')
            ], width=12),
        ]),
        # Add more components as needed
    ], fluid=True)
