#!/usr/bin/env python3

#In case of OSError: [Errno 8]
#https://stackoverflow.com/questions/55271912/flask-cli-throws-oserror-errno-8-exec-format-error-when-run-through-docker


import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

graph1 = dcc.Graph(
        id='example-barChart',
        figure={
            'data': [
                {'x': ['1999', '2009', '2019'], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': ['1999', '2009', '2019'], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Bar Chart Visualization'
            }
        }
    )
graph2 = dcc.Graph(
        id='example-pieChart',
        figure={
            'data': [
                {'labels': ['a', 'b', 'c'], 'values': [400, 100, 200], 'type': 'pie', 'name': 'SF'}
            ],
            'layout': {
                'title': 'Dash Pie Chart Visualization'
            }
        }
    )

upstream_style_dict = {'display':'flex',
                       'flex-direction':'row'
                        }

style_dict = {'width':'49%',
               'height':'20%',
               'flex-wrap':'wrap',
               'display':'inline-block'
               }

welcome_msg = "Dash: A web application framework for Python."
graph_dboard = html.Div(children=[
    welcome_msg,
    html.Div(children= [
        graph1,
        graph2
        ], style=style_dict)
    ],style=upstream_style_dict)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    graph_dboard
])

if __name__ == '__main__':
    app.run_server(debug=True)
