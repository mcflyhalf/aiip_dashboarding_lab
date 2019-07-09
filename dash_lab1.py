#!/usr/bin/env python3

#In case of OSError: [Errno 8]
#https://stackoverflow.com/questions/55271912/flask-cli-throws-oserror-errno-8-exec-format-error-when-run-through-docker



#plot 2 simple bar graphs- 2 generators

#!/usr/bin/env python3

#In case of OSError: [Errno 8]
#https://stackoverflow.com/questions/55271912/flask-cli-throws-oserror-errno-8-exec-format-error-when-run-through-docker


import dash
import dash_core_components as dcc 	#This library will give us the dashboard elements (pie charts, scatter plots, bar graphs etc)
import dash_html_components as html 	#This library allows us to arrange the elements from dcc in a page as is done using html (on the internet)

#Fancy Styles provided to us by dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May'] #Will form our x-axis later
p2_prod = [10,19,24,22,16]	#production of p2
p5_prod = [8,12,17,13,9]
p3_prod = [10,19,24,22,16]	#production of p2
p1_prod = [8,12,17,13,9]
p4_prod = [10,19,24,22,16]	#production of p2



bar2 = dcc.Graph(
        id='barChart-p2',
        figure={
            'data': [
                {'x': months, 'y': p2_prod, 'type': 'bar', 'name': 'P2'},
                {'x': months, 'y': p5_prod, 'type': 'bar', 'name': 'P5'},
                    ],
            'layout': {
                'title': 'Powerplant p2&p5 production'
            }
        }
    )

pie = dcc.Graph(
        id='pieChart-p2',
        figure={
            'data': [
                {'labels': ['p1', 'p2', 'p3', 'p4','p5'], 'values': [sum(p1_prod),sum(p2_prod),sum(p3_prod),sum(p4_prod),sum(p5_prod)], 'type': 'pie', 'name': 'prod_pie'},
                    ],
            'layout': {
                'title': 'Total Jan-May production'
            }
        }
    )

bar3 = dcc.Graph(
        id='barChart-p1-p3',
        figure={
            'data': [
                {'x': months, 'y': p1_prod, 'type': 'bar', 'name': 'P1'},
                {'x': months, 'y': p2_prod, 'type': 'bar', 'name': 'P2'},
                {'x': months, 'y': p3_prod, 'type': 'bar', 'name': 'P3'},
                    ],
            'layout': {
                'title': 'Powerplant p1-p3 production'
            }
        }
    )

pie3 = dcc.Graph(
        id='pieChart-p1-p3',
        figure={
            'data': [
                {'labels': ['p1', 'p2', 'p3'], 'values': [sum(p1_prod),sum(p2_prod),sum(p3_prod)], 'type': 'pie', 'name': 'prod_pie'},
                    ],
            'layout': {
                'title': 'Total Jan-May production (p1-p3)'
            }
        }
    )

# graph2 = dcc.Graph(
#         id='example-pieChart',
#         figure={
#             'data': [
#                 {'labels': ['a', 'b', 'c'], 'values': [400, 100, 200], 'type': 'pie', 'name': 'SF'}
#             ],
#             'layout': {
#                 'title': 'Dash Pie Chart Visualization'
#             }
#         }
#     )

app.layout = html.Div(children=[
    html.H1(children='ALU AIIP'),

    html.Div(children='''
        ACME inc's web dashboard. Built using Dash: A web application framework for Python.
    '''),
    bar3,
    pie3
])

#Do the same for p5

#plot the bar graphs together on the same axes. Compare p2 and p5.
# #Given that p2 and p5 are solar and in the same place, use your plots to determine:
# 1. Which is the later generation technology?
# 2. Which are the best 3 months for solar generation?






if __name__ == '__main__':
	app.run_server(debug=True)