from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

from app.save_princess.save_princess import save_princess
from app.save_princess.const import MOVES_DICT, UP, DOWN


def register_callbacks(dash_app):
    """ register a callback here """
    @dash_app.callback(
        Output('output-container', 'children'),
        [Input('button', 'n_clicks')],
        [State('size-n', 'value'), State('grid', 'value')])
    def update_output(n_clicks, n_value, grid_value):
        error_flag, path, validated_data = save_princess(n_value, grid_value, game_mode=True)
        if error_flag:
            return html.H2(children=f"{validated_data.message}. Please check your input and enter again")
        if not path:
            return html.H2(children="Mario has lost the game. Too many obstacles on his way.")
        x_points, y_points = form_points(validated_data, path)
        obstacles = list(zip(*validated_data.obstacles))
        if not obstacles:
            x_obstacles = []
            y_obstacles = []
        else:
            x_obstacles = list(obstacles[1])
            y_obstacles = list(obstacles[0])

        return html.Div(children=[
            html.H1(children='Mario Saved Princess!!!'),
            html.Div(children=" -> ".join(path)),
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=0), name='0th index'),
                        go.Scatter(x=[validated_data.mario_index[1]], y=[validated_data.mario_index[0]], mode='markers',
                                   marker=dict(size=20, color='blue'), name='Mario'),
                        go.Scatter(x=[validated_data.princess_index[1]], y=[validated_data.princess_index[0]],
                                   mode='markers', marker=dict(size=20, color='deeppink'), name='Princess'),
                        go.Scatter(x=x_obstacles, y=y_obstacles, mode='markers', marker=dict(size=20, color='red'),
                                   name='Obstacles'),
                        go.Scatter(x=x_points, y=y_points, line=dict(width=6), name='Path')
                    ],
                    layout=go.Layout(
                        xaxis=go.layout.XAxis(
                            tickmode='linear',
                            tick0=0,
                            dtick=1,
                            gridcolor='LightPink',
                        ),
                        yaxis=go.layout.YAxis(
                            tickmode='linear',
                            tick0=0,
                            dtick=1,
                            gridcolor='LightPink',
                            autorange="reversed"
                        ),

                        height=650,
                        width=650
                    ),
                )
            )
        ])


def form_points(data, path):
    """
    This method is used to return the row and column information of the path
    :param data: validated data
    :param path: path to princess
    :return: x-coordinates and y-coordinates
    """
    x_points = []
    y_points = []
    current_vertex = data.mario_index.copy()
    y_points.append(current_vertex[0])
    x_points.append(current_vertex[1])
    for move in path:
        if DOWN in move or UP in move:
            current_vertex[0] += MOVES_DICT[move]
        else:
            current_vertex[1] += MOVES_DICT[move]
        y_points.append(current_vertex[0])
        x_points.append(current_vertex[1])
    return x_points, y_points
