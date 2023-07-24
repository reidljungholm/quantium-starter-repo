import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_csv('formatted_output.csv', parse_dates=['Date'])
price_increase_date = pd.to_datetime('2021-01-15')
data_before_increase = df[df['Date'] < price_increase_date]

avg_sales_before = data_before_increase['Sales'].mean()
avg_sales_after = df[df['Date'] >= price_increase_date]['Sales'].mean()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Data Visualizer"),
    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [
                {'x': df['Date'], 'y': df['Sales'], 'type': 'line', 'name': 'Sales'},
                {'x': [price_increase_date, price_increase_date], 'y': [0, df['Sales'].max()], 'type': 'line', 'name': 'Price Increase'},
            ],
            'layout': {
                'title': 'Sales Trend Over Time',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Sales'},
                'plot_bgcolor': '#F9F9F9',
                'paper_bgcolor': '#F9F9F9',
                'legend': {'x': 0, 'y': 1},
            }
        }
    ),
    html.Div([
        html.H3("Average Sales (Before Pink Morsel Price Increase): {:.2f}".format(avg_sales_before)),
        html.H3("Average Sales (After Pink Morsel Price Increase): {:.2f}".format(avg_sales_after))
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)

