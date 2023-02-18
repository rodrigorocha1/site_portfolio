from dash import html
import dash_bootstrap_components as dbc


class CartoesFeed:

    def __init__(self):  # objeto app
        self._legendas = [
            ('Pokedex Primeira Versão - Python', 'id_title_feed_pokedex', 'Clique Aqui', 'id_btn_pokedex'),
            ('Eleições 2022-Versão Power BI', 'id_title_feed_el_2022', 'Clique Aqui', 'id_btn_eli'),
            ('Aplicativo Previsão Tempo', 'id_title_feed_pv', 'Clique Aqui', 'id_btn_tempo'),
            ('Sobre Mim', 'id_title_feed', 'Clique Aqui', 'id_btn_feedd')
        ]
        self.cartoes_feed = self._gerar_layout_feed()

    def _gerar_layout_feed(self):
        cartoes = []
        for nm_h4, id_h4, nm_botao, id_btn in self._legendas:
            cartao = dbc.Card(
                dbc.CardBody(
                    [
                        html.H4(nm_h4,
                                className='card-title',
                                id=f'{id_h4}'),
                        html.Button(nm_botao,
                                    className='class_btn_feed',
                                    id=f'{id_btn}')
                    ],
                    className='class_coluna_info'
                )
            )
            cartoes.append(dbc.Col(cartao, md=3))
        return [
            html.H5('Últimos Projetos', id='id_titulo_feed'),
            *cartoes
        ]
