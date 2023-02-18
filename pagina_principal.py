from dash import dcc, html, Output, Input, State, Dash
from paginas.pagina_apresentacao import PaginaApresentacao
from paginas.pagina_lista_projetos import PaginaListaProjetos
import dash_bootstrap_components as dbc
from componentes.habilidades import Habilidades
from componentes.cartoes_feed import CartoesFeed
from componentes.sobre_min import SobreMim


class PaginaPrincipal:

    def __init__(self):
        """
            Parâmetros para iniciar o layout
        """
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.layout = self.gerar_layout_principal()
        self._criar_calback_page()
        self.app.title = 'Apresentação'
        self.app.config['suppress_callback_exceptions'] = True
        self.app.scripts.config.serve_locally = True

    def gerar_layout_principal(self):
        """
            Método para gerar o navbar
        """
        navbar = html.Div(
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
                                self._navibar_principal(),
                                id='navbar-collapse',
                                is_open=False,
                                navbar=True,
                            ),
                        ]
                    ),

                    color='#141A32',
                    id='id_container'
                ),
                html.Div(id='page-content')
            ], id='id_main_div'
        )

        return navbar

    def rodar_aplicacao(self):
        """
            Método para rodar aplicação
        """
        self.app.run_server(debug=True, port=8044)

    def _navibar_principal(self):
        """
            Método para gerar o navbar e navegações
        """
        return dbc.Row(
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
                    ],
                    id='id_nav_bar'
                )
            ],
            className='g-0 ms-auto flex-nowrap mt-3 mt-md-0',
            id='id_nav_main'
        )

    def _toggle_navbar_collapse(self, n, is_open):
        """
            Método para colapsar a navbar
        @param n:
        @param is_open: aberto
        @return:
        """
        if n:
            return not is_open
        return is_open

    def _render_page_content(self, pathname):
        """
        Método para a troca da página
        @param pathname: recebe o id tab
        @return: a página gerada
        """
        if pathname == '/paginas/pagina_apresentacao' or pathname == '/':
            sm = SobreMim()
            ha = Habilidades()
            cf = CartoesFeed()
            pa = PaginaApresentacao(sobre_min=sm, habilidade=ha, cartoes_feed=cf)
            return pa.pagina_apresentacao
        elif pathname == '/paginas/lista_projetos':
            lp = PaginaListaProjetos()
            return lp.layout_lista_projetos
        else:
            return '404'

    def _criar_calback_page(self):
        """
            Método para criar os calbacks e suas funções
        """
        self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )(self._render_page_content)
        self.app.callback(
            Output('navbar-collapse', 'is_open'),
            [Input('navbar-toggler', 'n_clicks')],
            [State('navbar-collapse', 'is_open')],

        )(self._toggle_navbar_collapse)


# Start Página
pp = PaginaPrincipal()
server = pp.app.server

if __name__ == '__main__':
    pp.rodar_aplicacao()
