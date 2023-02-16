from dash import html
import dash_bootstrap_components as dbc


class CartoesFeed:

    def __init__(self):
        self.cartoes_feed = self.__gerar_cartoes_feed()

    def __gerar_cartoes_feed(self):
        primeiro_cartao = dbc.Card(
            dbc.CardBody(
                [
                    html.H4('Pokedex Primeira Versão - Python',
                            className='card-title',
                            id='id_title_feed_pokedex'),
                    html.Button('Clique Aqui',
                               className='class_btn_feed',
                               id='id_btn_pokedex')
                ],
                className='class_coluna_info'
            )
        )

        segundo_cartao = dbc.Card(
            dbc.CardBody(
                [
                    html.H4('Eleições 2022-Versão Power BI',
                            className='card-title',
                            id='id_title_feed_el_2022'),
                    html.Button('Clique Aqui',
                               className='class_btn_feed',
                               id='id_btn_eli')
                ],
                className='class_coluna_info'
            )
        )

        terceiro_cartao = dbc.Card(
            dbc.CardBody(
                [
                    html.H4('Aplicativo Previsão Tempo',
                            className='card-title',
                            id='id_title_feed_pv'),
                    html.Button('Clique Aqui',
                               className='class_btn_feed',
                               id='id_btn_tempo')
                ],
                className='class_coluna_info'
            )
        )

        quarto_cartao = dbc.Card(
            dbc.CardBody(
                [
                    html.H4('Sobre Mim',
                            className='card-title',
                            id='id_title_feed'),
                    html.Button('Clique Aqui',
                               className='class_btn_feed',
                               id='id_btn_feedd'
                               )
                ],
                className='class_coluna_info'
            )
        )

        return [
            html.H5('Últimos Projetos', id='id_titulo_feed'),
            dbc.Col(primeiro_cartao, md=3, ),
            dbc.Col(segundo_cartao, md=3, ),
            dbc.Col(terceiro_cartao, md=3, ),
            dbc.Col(quarto_cartao, md=3, ),
        ]


