import dash
import dash_core_components as dcc
import dash_html_components as html
from paginas.lista_projetos import ListaProjetos
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Clique aqui', id='my-button'),
    html.Div(id='output')
])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('my-button', 'n_clicks')],
    [dash.dependencies.State('my-button', 'id')])
def update_output(n_clicks, button_id):
    print(button_id)
    if button_id == 'my-button':
        lp = ListaProjetos()
        return lp.layout_lista_projetos


if __name__ == '__main__':
    app.run_server(debug=True)
