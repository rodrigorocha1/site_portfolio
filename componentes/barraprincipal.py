import dash_bootstrap_components as dbc


barra_principal = [
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    'Ínicio',
                    className='class_navbar'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'Projetos',
                    className='class_navbar'
                )
            )
        ],
        color='write',
        brand='Portfolio Rodrigo Silva Rocha',
        dark=True,
        id='id_navbar_main'
    ),
]
