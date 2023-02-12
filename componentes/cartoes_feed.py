from dash import html
import dash_bootstrap_components as dbc

primeiro_cartao = dbc.Card(
    dbc.CardBody(
        html.H5('Cartão 1')
    ), className='class_coluna_info'
)

segundo_cartao = dbc.Card(
    dbc.CardBody(
        html.H5('Cartão 2')
    ), className='class_coluna_info'
)

terceiro_cartao = dbc.Card(
    dbc.CardBody(
        html.H5('Cartão 3')
    ) , className='class_coluna_info'
)

quarto_cartao = dbc.Card(
    dbc.CardBody(
        html.H5('Cartão 3')
    ), className='class_coluna_info'
)

quinto_cartao = dbc.Card(
    dbc.CardBody(
        html.H5('Cartão 3')
    ), className='class_coluna_info'
)
