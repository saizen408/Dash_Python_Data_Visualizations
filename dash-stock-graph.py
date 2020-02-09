import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime.now()
stock = 'TSLA'
df = web.DataReader(stock, 'yahoo', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='symbol to graph'),
    dcc.Input(id='input', value='tsla', type='text'),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index,
                 'y': df.Close,
                 'type': 'line',
                 'name': input_data
                 }
            ],
            'layout': {
                'title': input_data
            }
        }
    )


print(df)
print(df.index)

if __name__ == '__main__':
    app.run_server(debug=True)


# html of the entire app
# app.layout = html.Div(children=[
#     dcc.Input(id='input', value='Enter something', type='text'),
#     html.Div(id='output')
# ])
# @app.callback(
#     Output(component_id='output', component_property='children'),
#     [Input(component_id='input', component_property='value')]
# )
# def update_value(input_data):
#     try:
#         return str(float(input_data)**2)
#         # return "Input: {}".format(input_data)
#     except:
#         return "Some error"