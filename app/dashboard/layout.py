import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.H1('Dashboard', style={'backgroundColor': 'lightblue'}),
    dcc.Input(
        placeholder='size',
        id='size-n',
        type='number',
        value='',
        style={'backgroundColor': 'lightblue', 'width': 60}
    ),
    dcc.Input(
        placeholder='Grid Example --m,-x-,-p-',
        id='grid',
        value='',
        style={'backgroundColor': 'lightblue', 'width': 500}
    ),
    html.Button('Find Princess', id='button',
                style={'boxShadow': '0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19)'}),
    html.Div(id='output-container',
             children='Enter values and press the button'),

])
