from plotly_bar import bar_fig
import dash
from dash import dcc

app = dash.Dash()

app.layout = dcc.Graph(
    id='example-graph',
    figure=bar_fig
)

if __name__ == '__main__':
    app.run(debug=True)