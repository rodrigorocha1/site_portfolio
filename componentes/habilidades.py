from dash import html
import dash_bootstrap_components as dbc


class Habilidades:

    def __init__(self):
        """

        """
        self.__lista_habilidades = [
            (' - Pentaho ',
             'https://yt3.ggpht.com/ytc/AMLnZu-zHYbfICJDEel0ighDFOcAN4KklMhvHzwaLlbg=s900-c-k-c0x00ffffff-no-rj'),
            (' - Sql Server ', 'https://www.freeiconspng.com/uploads/sql-server-icon-png-8.png'),
            (' - Python ', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'),
            (' - Power BI ', 'https://github.com/microsoft/PowerBI-Icons/raw/main/PNG/Power-BI.png'),
            (' - Oracle ', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/oracle/oracle-original.svg'),
            (' - Dash e Plotly ', 'https://www.vectorlogo.zone/logos/plot_ly/plot_ly-official.svg'),
        ]

        self.__lista_contatos = [
            ('Git', 'assets/git.png', 'https://github.com/rodrigorocha1'),
            ('Linkedin', 'assets/link.png', 'https://www.linkedin.com/in/rodrigo-rocha-dados/')
        ]

        self.cards_habilidades = self.__gerar_card_habilidade()

    def __gerar_lista_apresentacao(self):
        """
            Método para gera a lista de apresentação
        """
        return [
            html.Li(
                [
                    html.Img(
                        src=url_img,
                        alt=nome,
                        className='class_lista_imagens',
                        id=f'id_img_{nome}'
                    ),
                    nome
                ], id=f'id_lista_{nome}'
            )
            for nome, url_img in self.__lista_habilidades
        ]

    def __gerar_card_habilidade(self):
        """
            Método para gerar os cards com habilidades
        """
        return dbc.Card(
            dbc.CardBody(
                [
                    html.H4(
                        'Habilidades',
                        className='class_cor_fundo'
                    ),
                    html.Div(
                        html.Ul(
                            self.__gerar_lista_apresentacao()
                        )
                    ),
                    html.H4('Contatos', className='class_cor_fundo'),
                    html.Div(
                        [
                            html.A(
                                [
                                    html.Img(
                                        src=path_img,
                                        width='40px',
                                        height='40px'
                                    ) for nome_contato, path_img, url_contato in self.__lista_contatos
                                ]
                            )
                        ],
                        id='id_img_contatos'
                    )
                ],
                className='class_coluna_info'
            )
        )
