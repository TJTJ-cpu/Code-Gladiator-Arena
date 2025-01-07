# importing required libraries 
import dash 
from dash import html
from dash import dcc


app = dash.Dash() 

app.layout = html.Div(children =[ 
	html.H1("Dash Tutorial"), 
	dcc.Graph( 
		id ="example", 
		figure ={ 
			'data':[ 
					{'x':[1, 2, 3, 4, 5], 
						'y':[5, 4, 7, 4, 8], 
						'type':'line', 
						'name':'Trucks'}, 
					{'x':[1, 2, 3, 4, 5], 
						'y':[6, 3, 5, 3, 7], 
						'type':'bar', 
						'name':'Ships'} 
				], 
			'layout':{ 
				'title':'Basic Dashboard'
			} 
		} 
	) 
]) 

