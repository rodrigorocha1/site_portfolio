from dash import dcc, html
from app import *
import dash_bootstrap_components as dbc
from componentes.barraprincipal import barra_principal

content = html.Div(id='id_page_content')

app.layout = html.Div(
    [
        dbc.Row(
            barra_principal,
            id='id_linha_principal_um'
        ),
        dbc.Row(
            [
                dbc.Col(
                    'Primeira Coluna',
                    md=4,
                    className='class_coluna_info'
                ),
                dbc.Col(
                    'Minhas Habilidades',
                    md=4,
                    className='class_coluna_info'
                ),
                dbc.Col(
                    'Minhas Habilidades',
                    md=4,
                    className='class_coluna_info'
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
