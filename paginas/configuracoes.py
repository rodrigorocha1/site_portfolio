from dash import Dash
import dash_bootstrap_components as dbc


class Configuracoes:
    def __init__(self):
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.config['suppress_callback_exceptions'] = True
        self.app.scripts.config.serve_locally = True

