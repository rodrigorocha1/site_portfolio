from dash import dcc, html
from app import *
import dash_bootstrap_components as dbc
from componentes.barraprincipal import barra_principal

content = html.Div(id='id_page_content')

app.layout = html.Div(
    [
        dbc.Row(
            barra_principal
        ),
        dbc.Row(
            [
                dbc.Col('Primeira Coluna', md=6),
                dbc.Col('Segunda Coluna', md=6)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
