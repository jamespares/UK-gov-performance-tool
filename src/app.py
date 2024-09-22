# src/app.py

import dash
import dash_bootstrap_components as dbc
from dash import html
import yaml

# Load the config.yaml file
with open("app_config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

from src.layout import layout
from src.callbacks import register_callbacks

# Initialize Dash app with Bootstrap theme
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server  # Expose the server variable for deployments

# Set the layout
app.layout = layout

# Register callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=config['app']['debug'], port=config['app']['port'])
