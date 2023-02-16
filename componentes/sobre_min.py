from dash import html
import dash_bootstrap_components as dbc


class SobreMim:
    def __init__(self):
        self.layout_sobre_mim = self.__gerar_layout_sobre_min()

    def __gerar_layout_sobre_min(self):
        return dbc.Card(
            dbc.CardBody(
                [
                    html.H4('Sobre Mim',
                            className='card-title',
                            id='id_title'),
                    html.P('Hoje trabalho com Pentaho data Integration,'
                           ' SQL (Consulta Simples No Banco de dados)'
                           ' Consumo de API (REST E SOAP)',
                           className='class_paragrafo',
                           id='id_paragrafo_um'),
                    html.H4('Formação Acadêmica',
                            className='card-title'),
                    html.P('Formado em  Análise e Desenvolvimento de Sistemas '
                           'na Fatec (Faculdade de Tecnologia de Ribeirão Preto), conclusão em 2020.',
                           className='class_paragrafo',
                           id='id_paragrafo_dois'),
                    html.H4('TCC',
                            className='card-title'),
                    html.A(
                        'Implementando o Processo de ETL (Extract, Transform And Load) '
                        ' Para a Análise de Variáveis '
                        ' Pertinentes a um Dataset Oriundo da Plataforma de '
                        ' Dados Abertos do Governo Federal no que Tange as '
                        ' Reclamações Realizadas Entre os Anos de 2017 e 2018',
                        href='http://www.fatecrp.edu.br/WorkTec/edicoes/2020-2/trabalhos/II-Worktec'
                             '-Rodrigo_Rocha.pdf',
                        className='class_paragrafo',
                        id='id_link'
                    )
                ],
                className='class_coluna_info'
            )
        )
