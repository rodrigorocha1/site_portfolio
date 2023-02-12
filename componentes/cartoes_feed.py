from dash import html
import dash_bootstrap_components as dbc

primeiro_cartao = dbc.Card(
    dbc.CardBody(
        [
            html.H4('Pokedex Primeira Versão - Python',
                    className='card-title',
                    id='id_title_feed'),
            dbc.Button('Projeto',
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
                    id='id_title_feed'),
            dbc.Button('Projeto',
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
                    id='id_title_feed'),
            dbc.Button('Projeto',
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
            dbc.Button('Projeto',
                       className='class_btn_feed',
                       id='id_btn_tempo'
                       )
        ],
        className='class_coluna_info'
    )
)
