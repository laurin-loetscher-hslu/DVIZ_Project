from dash import Input, Output
import plotly.express as px
from src.data_loader import prepare_data

df = prepare_data()

def register_callbacks(app):
    @app.callback(
        Output('disease-pie-chart', 'figure'),
        Output('disease-bar-chart', 'figure'),
        Input('incident-map', 'clickData')
    )
    def update_charts(clickData):
        if clickData is None:
            return {}, {}

        country = clickData['points'][0]['location']
        filtered = df[df['country'] == country]

        if filtered.empty:
            return {}, {}

        # Pie chart data
        pie_data = filtered.groupby('disease').size().reset_index(name='count')
        pie_fig = px.pie(
            pie_data,
            names='disease',
            values='count',
            title=f"Disease Distribution in {country}"
        )

        # Bar chart data (time series)
        bar_data = filtered.groupby(['year', 'country']).size().reset_index(name='count')
        bar_fig = px.bar(
            bar_data,
            x='year',
            y='count',
            barmode='group',
            title=f"Disease Trend Over Time in {country}"
        )

        return pie_fig, bar_fig

#def register_callbacks(app):
#    @app.callback(
#        Output('disease-pie-chart', 'figure'),
#        Input('incident-map', 'clickData')
#    )
#    def update_pie_chart(clickData):
#        if clickData is None:
#            return {}
#
#        # Extract country name from clickData
#        country = clickData['points'][0]['location']
#        filtered = df[df['country'] == country]
#
#        if filtered.empty:
#            return {}
#
#        pie_data = filtered.groupby('disease').size().reset_index(name='count')
#        pie_fig = px.pie(
#            pie_data,
#            names='disease',
#            values='count',
#            title=f"Disease Distribution in {country}"
#        )
#        return pie_fig
