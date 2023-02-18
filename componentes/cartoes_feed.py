from dash import html
import dash_bootstrap_components as dbc


class CartoesFeed:

    def __init__(self):
        """
            Construtor com os atributos legendas e cartões feed
        """
        self._legendas = [
            ('Pokedex Primeira Versão - Python', 'id_title_feed_pokedex', 'Clique Aqui', 'id_btn_pokedex'),
            ('Eleições 2022-Versão Power BI', 'id_title_feed_el_2022', 'Clique Aqui', 'id_btn_eli'),
            ('Aplicativo Previsão Tempo', 'id_title_feed_pv', 'Clique Aqui', 'id_btn_tempo'),
            ('Sobre Mim', 'id_title_feed', 'Clique Aqui', 'id_btn_feedd')
        ]
        self.cartoes_feed = self._gerar_layout_feed()

    def _gerar_layout_feed(self):

        """
            Gera o layout com os projetos
        @return: Uma coluna com cartões
        """

        cartoes = [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                nm_h4,
                                className='card-title',
                                id=f'{id_h4}'
                            ),
                            dbc.CardLink('external link', className='class-link-externo')
                        ],
                        className='class_coluna_info'
                    )
                ),
                md=3
            ) for nm_h4, id_h4, nm_botao, id_btn in self._legendas
        ]
        return [
            html.H5('Últimos Projetos', id='id_titulo_feed'),
            *cartoes
        ]
