from dash import dcc, html
from app import *
import dash_bootstrap_components as dbc


content = html.Div(id='id_page_content')

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink('pg1', href='#')),
                        dbc.NavItem(dbc.NavLink('pg2'))
                    ],
                    color='black',
                    brand='NavbarSimple',
                    dark=True
                ),


            ]
        ),
        dbc.Row('     Segunda  Linhas')
    ]
)

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
