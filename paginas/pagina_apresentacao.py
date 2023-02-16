from componentes.habilidades import Habilidades
from componentes.cartoes_feed import CartoesFeed
from componentes.sobre_min import SobreMim
import dash_bootstrap_components as dbc


class PaginaApresentacao:
    def __init__(self, sobre_min: SobreMim, habilidade: Habilidades, cartoes_feed: CartoesFeed):
        self.__cartoes_feed = cartoes_feed
        self.__habilidade = habilidade
        self.__sobre_min = sobre_min

        self.pagina_apresentacao = self.__gerar_pagina_apresentacao(
            self.__sobre_min,
            self.__habilidade,
            self.__cartoes_feed

        )

    def __gerar_pagina_apresentacao(self, sobre_min: SobreMim, habilidade: Habilidades, cartoes_feed: CartoesFeed):
        return [
            dbc.Row(
                [
                    dbc.Col(sobre_min.layout_sobre_mim, md=6),
                    dbc.Col(habilidade.cards_habilidades, md=6)
                ]
            ),
            dbc.Row(
                cartoes_feed.cartoes_feed
            )
        ]

