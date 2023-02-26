from dash import Dash, html, Input, Output
import dash_daq as daq

app = Dash(__name__)

app.layout = html.Div([
    daq.BooleanSwitch(id='our-boolean-switch', on=False),
    html.Div(id='boolean-switch-result')
])


@app.callback(
    Output('boolean-switch-result', 'children'),
    Input('our-boolean-switch', 'on')
)
def update_output(on):
    return f'The switch is {on}.'


if __name__ == '__main__':
    app.run_server(debug=True)
