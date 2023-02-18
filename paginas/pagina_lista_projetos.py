from dash import html, dcc
import dash_bootstrap_components as dbc


class PaginaListaProjetos:

    def __init__(self):
        """
            Construtor com os parámetros
        """
        self._legendas_projetos = [
            ('', 'id_img2', 'Titulo', 'id_titulo2', 'desc', 'id_desc2', 'link', 'id_link_2'),
            ('', 'id_img3', 'Titulo', 'id_titulo3', 'desc', 'id_desc3', 'link', 'id_link_3'),
            ('', 'id_img4', 'Titulo', 'id_titulo4', 'desc', 'id_desc4', 'link', 'id_link_4'),
            ('', 'id_img5', 'Titulo', 'id_titulo5', 'desc', 'id_desc5', 'link', 'id_link_5'),
            ('', 'id_img6', 'Titulo', 'id_titulo6', 'desc', 'id_desc6', 'link', 'id_link_6'),
            ('', 'id_img7', 'Titulo', 'id_titulo7', 'desc', 'id_desc7', 'link', 'id_link_7'),
            ('', 'id_img8', 'Titulo', 'id_titulo8', 'desc', 'id_desc8', 'link', 'id_link_8'),
            ('', 'id_img1', 'Pokedex Primeira Versão',
             'id_pokedex_primeira_versao',
             'Pokedex V1 feita, sem controle de repetição de código, ou seja, o padrão de código aqui, viola os '
             'principios SOLID',
             'id_desc_pokedex', 'link',
             'id_link_pokedex'),
        ]
        self.layout_lista_projetos = self._gerar_lista_projetos()

    def _gerar_lista_projetos(self):
        """
        Método para gerar a lista de cartões para a galeria
        @return: uma linha com cartões
        """
        cartoes_projeto = []
        for caminho_img, id_img, titulo_cartao, id_titulo, desc, id_desc, link, id_link in self._legendas_projetos:
            card_lista_projeto = \
                dbc.Card(
                    [
                        dbc.CardImg(
                            src=caminho_img,
                            top=True,
                        ),
                        dbc.CardBody(
                            [
                                html.H4(
                                    titulo_cartao,
                                    id=id_titulo,
                                    className='card-title'
                                ),
                                html.P(
                                    desc,
                                    id=id_desc,
                                    className='card_text',
                                )
                            ]
                        )
                    ], className='class_coluna_info'
                )
            cartoes_projeto.append(
                dbc.Col(
                    card_lista_projeto,
                    md=3,
                    className='class_card_projeto'
                ),
            )
        return html.Div(
            [
                dbc.Row(
                    html.H5('Galeria de projetos', id='id_titulo_feed'),
                ),
                dbc.Row(
                    cartoes_projeto,
                    className='class_linha_projeto'
                ),
            ]
        )
