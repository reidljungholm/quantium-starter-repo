import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_csv('formatted_output.csv', parse_dates=['Date'])
price_increase_date = pd.to_datetime('2021-01-15')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Data Visualizer", style={'text-align': 'center'}),
    
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
        ],
        value='all',
        labelStyle={'display': 'block', 'margin': '10px'},
    ),
    
    dcc.Graph(
        id='sales-line-chart',
        config={'displayModeBar': False},
    ),
    
    html.Div(style={'height': '30px'}),
    
    html.Div([
        html.H3(id='avg-sales-before'),
        html.H3(id='avg-sales-after')
    ], style={'text-align': 'center'}),
    
], style={'padding': '20px', 'font-family': 'Arial, sans-serif'})

@app.callback(
    [dash.dependencies.Output('sales-line-chart', 'figure'),
     dash.dependencies.Output('avg-sales-before', 'children'),
     dash.dependencies.Output('avg-sales-after', 'children')],
    [dash.dependencies.Input('region-selector', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'all':
        data_filtered = df
    else:
        data_filtered = df[df['Region'] == selected_region]
        
    data_before_increase = data_filtered[data_filtered['Date'] < price_increase_date]
    data_after_increase = data_filtered[data_filtered['Date'] >= price_increase_date]
    
    avg_sales_before = data_before_increase['Sales'].mean()
    avg_sales_after = data_after_increase['Sales'].mean()
    
    line_chart = {
        'data': [
            {'x': data_filtered['Date'], 'y': data_filtered['Sales'], 'type': 'line', 'name': 'Sales'},
            {'x': [price_increase_date, price_increase_date], 'y': [0, data_filtered['Sales'].max()],
             'type': 'line', 'name': 'Price Increase'},
        ],
        'layout': {
            'title': f'Sales Trend Over Time - Region: {selected_region.upper() if selected_region != "all" else "All"}',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales'},
            'plot_bgcolor': '#F9F9F9',
            'paper_bgcolor': '#F9F9F9',
            'legend': {'x': 0, 'y': 1},
        }
    }
    
    return line_chart, f"Average Sales (Before Pink Morsel Price Increase): {avg_sales_before:.2f}", \
           f"Average Sales (After Pink Morsel Price Increase): {avg_sales_after:.2f}"

if __name__ == '__main__':
    app.run_server(debug=True)

