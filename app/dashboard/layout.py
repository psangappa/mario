import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.H1('Dashboard', style={'backgroundColor': 'lightblue'}),
    dcc.Input(
        placeholder='Enter the size of the grid',
        id='size-n',
        type='number',
        value='',
        style={'backgroundColor': 'lightblue'}
    ),
    dcc.Input(
        placeholder='Grid Example --m,-x-,-p-',
        id='grid',
        type='text',
        value='',
        style={'backgroundColor': 'lightblue'}
    ),
    html.Button('Submit', id='button',
                style={'boxShadow': '0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19)'}),
    html.Div(id='output-container',
             children='Enter a value and press submit'),

])
