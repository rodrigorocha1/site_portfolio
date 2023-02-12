from dash import dcc, html
from app import *
import dash_bootstrap_components as dbc
from componentes.barraprincipal import barra_principal

content = html.Div(id='id_page_content')

app.layout = html.Div(
    [
        dbc.Row(
            barra_principal,
            id='id_linha_principal_um'
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
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
                                html.P('Formado em  Análise e Desenvolvimento de Sistemas.'
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
                                    href='http://www.fatecrp.edu.br/WorkTec/edicoes/2020-2/trabalhos/II-Worktec-Rodrigo_Rocha.pdf',
                                    className='class_paragrafo',
                                    id='id_link'
                                )
                            ],
                            className='class_coluna_info'
                        )
                    ),
                    md=6,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4(
                                    'Habilidades',
                                    className='class_cor_fundo'
                                ),
                                html.Div(
                                    html.Ul(
                                        children=[
                                            html.Li(
                                                [
                                                    html.Img(
                                                        src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg',
                                                        className='class_lista_imagens',
                                                        alt='Python',
                                                        id='id_img_python'
                                                    ),
                                                    ' PYTHON'
                                                ], id='id_lista_python'
                                            ),
                                            html.Li(
                                                [
                                                    html.Img(
                                                        src='https://github.com/microsoft/PowerBI-Icons/raw/main/PNG/Power-BI.png',
                                                        alt='Power BI',
                                                        className='class_lista_imagens',
                                                        id='id_img_power_bi'
                                                    ),
                                                    ' POWER BI'
                                                ], id='id_lista_power_bi'
                                            ),
                                            html.Li(
                                                [
                                                    html.Img(
                                                        src='https://yt3.ggpht.com/ytc/AMLnZu-zHYbfICJDEel0ighDFOcAN4KklMhvHzwaLlbg=s900-c-k-c0x00ffffff-no-rj',
                                                        alt='Pentaho',
                                                        className='class_lista_imagens',
                                                        id='id_img_pentaho'
                                                    ),
                                                    ' PENTAHO'
                                                ], id='id_lista_pentaho'
                                            ),
                                            html.Li(
                                                [
                                                    html.Img(
                                                        src='https://www.freeiconspng.com/uploads/sql-server-icon-png-8.png',
                                                        alt='sql server',
                                                        className='class_lista_imagens',
                                                        id='id_img_sql_server'
                                                    ),
                                                    ' SQL SERVER'
                                                ], id='id_lista_sql_server'
                                            ),
                                            html.Li(
                                                [
                                                    html.Img(
                                                        src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/oracle/oracle-original.svg',
                                                        alt='Oracle',
                                                        className='class_lista_imagens',
                                                        id='id_img_oracle'
                                                    ),
                                                    ' ORACLE'
                                                ], id='id_lista_oracle_'
                                            ),
                                            html.Li(
                                                [
                                                    html.Img(
                                                        src='https://www.vectorlogo.zone/logos/plot_ly/plot_ly-official.svg',
                                                        alt='Dash',
                                                        className='class_lista_imagens',
                                                        id='id_img_dash'
                                                    ),
                                                    ' DASH'
                                                ], id='id_lista_dash'
                                            ),
                                        ]
                                    )
                                ),
                            ],
                            className='class_coluna_info'
                        )
                    ),
                    md=6,
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
