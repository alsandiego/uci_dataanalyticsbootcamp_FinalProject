# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import dash_table
import pandas as pd
import datetime

## Bootstrap CSS ##
external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

df = pd.read_csv('https://bootcamp-twitter-sentiment-analysis.s3-us-west-1.amazonaws.com/Practice_5.csv')
restaurant_list = df.Search_Term.unique()

available_indicators = df['Search_Term'].unique()

df['Time'] = pd.to_datetime(df['Time']).apply(lambda x: x - datetime.timedelta(hours=7))

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'Sentiment Analysis'

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Dataframe with Negative Tweets
df_Neg = pd.DataFrame(columns=df.columns)
neg_Condition = df.Result=="negative"
neg_Rows = df.loc[neg_Condition, :]
df_Neg = df_Neg.append(neg_Rows, ignore_index=True)
negative_count = df_Neg.groupby('Search_Term').size()


# Dataframe with Positive Tweets
df_Pos = pd.DataFrame(columns=df.columns)
pos_Condition = df.Result=="positive"
pos_Rows = df.loc[pos_Condition, :]
df_Pos = df_Pos.append(pos_Rows, ignore_index=True)
positive_count = df_Pos.groupby('Search_Term').size()

app.layout = html.Div(
	style={'backgroundColor': colors['background']}, 
	children=[

## Heading row ##
    html.Div(
        [
            html.H1(children='Fast Food Restaurant Sentiment Analysis',
                    className='twelve columns',
                    style={
                            'textAlign': 'center',
                            'color': colors['text'],
                            },
                    )            
        ], className="row"
    ),
## Multi-Value Dropdown ##
    html.Div([html.Hr(),], className="row"),
    html.Div(
        [
            html.Div(children='Select a Restaurant',
                    style={
                            'color': 'white',
                            'textAlign': 'center'
                            },
                    ),

            html.Div(
            	dcc.Dropdown(
            		id='dropdown-selection', 
            		value="kfc", 
            		clearable=False,
            		options=[
            			{'label': i, 'value': i} for i in available_indicators],
            			),

            		),
    
        ], 	style={'width': '30%', 'float': 'center', 'display': 'inline-block', 'fontWeight': 'bold', 'color': 'blue', 'align-items': 'center'},
        	className="four columns offset-by-four"
    ),
    

## Row of Sentiment Percentages ##
    html.Br(),

    html.Div(
    	[
    		html.H3(    	
    			id='restaurant_selection',
    			className='twelve columns',
    			style={
                            'color': colors['text'],
                            'textAlign': 'center'
                            },
                    )
    	], className="row"
    	),
    html.Div(
        [
        html.Div(
            children=[
            html.H3(children="Positive Tweets",
            		style={
            			'color': 'orange',
            			'textAlign': 'center'
            		},
            		className='six columns'),
            html.H3(children="Negative Tweets",
                    style={
                        'color': 'orange',
                        'textAlign': 'center'
                    },
                    className='six columns'),
            ]),
        html.Div(children=[
            html.H4(
            	id='pos_tweet_detail',
            	style={
                        'color': 'orange',
                        'textAlign': 'center'
                    },
               className='six columns' 
                ), 
            html.H4(
            	id='neg_tweet_detail',
            	style={
                        'color': 'orange',
                        'textAlign': 'center'
                    },
                className='six columns'
                )
            
            ]
            ),
        ], className='row'  
    ),

## Graph Row ##

    html.Div(
        [
            dcc.Graph(
                    id='graph1',
                    className='four columns',
                    ),

             dcc.Graph(
                    id='graph2',
                    className='eight columns',
                    ),
        ], className="row"
    ),

## Graph Row 2 (combined restaurant graph)##
    html.Hr(),
    html.Div(
        [

             dcc.Graph(
                    className='twelve columns',
                     figure={
                        'data': [
                            {'x': restaurant_list, 'y': positive_count, 'type': 'bar', 'name': 'Positive'},
                            {'x': restaurant_list, 'y': negative_count, 'type': 'bar', 'name': 'Negative'},                     
                                ],
                        'layout': {
                            'title': 'Combined Restaurant Sentiment Totals',
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {
                                'color': colors['text'],
                                },
                            'xaxis': {
                            	'title': 'Restaurant Name'
                            },
                            'yaxis': {
                            	'title': 'Sentiment Percentages'
                            },
                            }
                        }
                    ),
        ], className="row"
    ),

## Data Table ##
    html.Div(
        [
            dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i, "hideable": "first"} for i in df.columns],
                    data=df.to_dict('records'),
                    page_size=15,
                    style_as_list_view=True,
                    style_header={
                            'backgroundColor': 'rgb(59, 57, 57)'},
                    style_cell={
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': 'white',
                            'textAlign': 'left'
                                },
                    ),
        ], className="row"
    ),

],)

#### This updates what restaurant we are viewing data for 
@app.callback(
	Output('restaurant_selection', 'children'),
	[Input('dropdown-selection', 'value')])

def update_output(value):
	return 'Sentiment for {}'.format(value)

#### This updates what the positve percentages are
@app.callback(
	Output('pos_tweet_detail', 'children'),
	[Input('dropdown-selection', 'value')])
def update_pos_tweet_percentage (selector):
	pos_result = positive_count.get(key = selector)
	neg_result = negative_count.get(key = selector)
	return str(round(pos_result/(pos_result+neg_result)*100))+"%"

#### This updates what the negative percentages are
@app.callback(
	Output('neg_tweet_detail', 'children'),
	[Input('dropdown-selection', 'value')])

def update_neg_tweet_percentage (selector):
	pos_result = positive_count.get(key = selector)
	neg_result = negative_count.get(key = selector)
	return str(round(neg_result/(pos_result+neg_result)*100))+"%"

#### This is updates the pie chart
@app.callback(
    Output('graph1', 'figure'),
    [Input('dropdown-selection', 'value')])

def update_graph1 (selector):
	pos_result = positive_count.get(key = selector)
	neg_result = negative_count.get(key = selector)
	print(pos_result, neg_result)
	return{
            'data': [
             	{
                'labels': ('positive', 'negative'),
                'values': (pos_result, neg_result),
                'type': 'pie',
                'marker': {'colors': ('yellow', '#ad1c4f')}
                },
                    ], 
                'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'margin': {
         	               'l': 40,
                            'r': 0,
                            'b': 40,
                            't': 0
                            },
                'showlegend': 'false'
                }
		}
    
#### This is updates the 2nd graphic
@app.callback(
    Output('graph2', 'figure'),
    [Input('dropdown-selection', 'value')])

def update_graph2 (selector):
	print(selector)

	search_df = pd.DataFrame(columns=df.columns)
	search_Condition = (df.Search_Term==selector)
	newSearch_df = df.loc[search_Condition, :]
	new_df = newSearch_df[['Time', 'Score']]
	
	return{
	        'data': [
                dict(
           	        x= new_df['Time'],
                    y= new_df.Score,
                    type='bar',                           
                    mode='markers',
                    opacity=0.7,
                    marker={
                           'size': 5,
                           'line': {'width': 0.1, 'color': 'white'},
                           'color': '#d62728'
                            },
                    ) 
                        ],
            'layout': {
                    'color': '#2ca02c, #d62728',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                            'color': colors['text'],
                            },
                    'xaxis': {
                           	'title': 'Tweet Time'
    	               		 }
                    }
                            
            }
    


if __name__ == '__main__':
    app.run_server(debug=True)