# src/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

def layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("UK Gov. Performance Dashboard"), width=12)
        ]),
        dbc.Row([
            dbc.Col([
                html.Label("Select Department"),
                dcc.Dropdown(
                    id='department-dropdown',
                    options=[
                        {'label': 'Department of Health and Social Care', 'value': 'health_social_care'},
                        {'label': 'Department for Education', 'value': 'education'},
                        {'label': 'Ministry of Defence', 'value': 'defence'},
                        {'label': 'Scotland Office', 'value': 'scotland'},
                        {'label': 'Department for Transport', 'value': 'transport'},
                        {'label': 'Home Office', 'value': 'home_office'},
                        {'label': 'Wales Office', 'value': 'wales'},
                        {'label': 'Northern Ireland Office', 'value': 'northern_ireland'},
                        {'label': 'Department for Science, Innovation and Technology', 'value': 'science_tech'},
                        {'label': 'Ministry of Justice', 'value': 'justice'},
                        {'label': 'Foreign, Commonwealth and Development Office', 'value': 'foreign_commonwealth'}
                    ],
                    value='education',  # Default to Education
                    clearable=False,
                    searchable=True,
                    style={'width': '600px'}  # Adjust the dropdown width to fit longer text
                )
            ], width=6),  # Adjust the column width as needed
        ], className="mb-4"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='time-series-chart')  # Updated time series chart
            ], width=12),
        ])
    ], fluid=True)