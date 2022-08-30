import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Nexflix Ratings'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/samanthabretouswork/project-8.git'
# here's the list of possible columns to choose from.



########## Set up the chart

import pandas as pd
df = pd.read_csv('data/netflix_titles.csv')
newdf =df.groupby(['rating'], as_index=False)['country'].count()

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Nexflix Movies by rating'),
    html.Div([
        html.Div([dcc.Graph(figure={
            "data": [{
                "x": newdf['rating'],
                "y": newdf['country'],
                "type": "bar"
            }],
            "layout": {
                "title": "Nexflix Movies by rating"
            }
        }),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
