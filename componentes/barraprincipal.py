import dash_bootstrap_components as dbc


barra_principal = [
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    'pg1',
                    className='class_navbar'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'pg2',
                    className='class_navbar'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'pg3',
                    className='class_navbar'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'pg4',
                    className='class_navbar'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'pg5',
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
