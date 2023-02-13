from dash import dcc, html, Output, Input, State
from paginas.pagina_apresentacao import pagina_apresentacao
from paginas.lista_projetos import lista_projetos
import dash
import dash_bootstrap_components as dbc


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server


navbar_principal = dbc.Row(
    [
        dbc.Nav(
            children=[
                dbc.NavItem(
                    dbc.NavLink(
                        'Inicio',
                        href='/paginas/pagina_apresentacao',
                        id='id_pg_inicio',
                        style={'color': '#FFFFFF'}
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        'Galeria de Projetos',
                        href='/paginas/lista_projetos',
                        id='id_pg_projetos',
                        style={'color': '#FFFFFF'}
                    )
                )
            ]
        )
    ],
    className='g-0 ms-auto flex-nowrap mt-3 mt-md-0',
    id='id_nav_main'
)

app.layout = html.Div(
    [
        dcc.Location(id='url'),
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.NavbarBrand(
                                        'Portifolio Rodrigo Silva Rocha',
                                        className='ms-2',
                                        style={'color': '#FFFFFF'}
                                    )
                                ),
                            ],
                            align='center',
                            className='g-0',
                        ),
                    ),
                    dbc.NavbarToggler(
                        id='navbar-toggler',
                        n_clicks=0
                    ),
                    dbc.Collapse(
                        navbar_principal,
                        id='navbar-collapse',
                        is_open=False,
                        navbar=True,
                    ),
                ]
            ),
            style={},
            color='#141A32',
            id='id_container'
        ),
        html.Div(id='page-content')
    ]
)


@app.callback(
    Output('navbar-collapse', 'is_open'),
    [Input('navbar-toggler', 'n_clicks')],
    [State('navbar-collapse', 'is_open')],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    print('pathname', pathname)
    if pathname == '/paginas/pagina_apresentacao' or pathname == '/':
        return pagina_apresentacao
    elif pathname == '/paginas/lista_projetos':
        return lista_projetos
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
