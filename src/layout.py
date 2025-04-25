import plotly.express as px
from dash import html, dcc
from src.data_loader import prepare_data

df = prepare_data()

# MAP
summary = df.groupby('country', as_index=False).count()

map_fig = px.choropleth(
    summary,
    locations='country',
    locationmode='country names',
    color='confirmed_cases',
    color_continuous_scale='Reds',
    title=f"Confirmed Cases of disease per country"
)

map_fig.update_geos(showframe=False, showcoastlines=False)

# fuck this shit, the zoom is horrible
map_fig.update_layout(
    geo=dict(
        projection_type="natural earth",
        projection_scale=1.2,
        center={"lat": 20, "lon": 0},
        showcountries=True
    ),
    margin={"r": 0, "t": 30, "l": 0, "b": 0},
    autosize=True
)

layout = html.Div([
    html.H1("Global Animal Health Incident Reports"),
    dcc.Graph(id='incident-map', figure=map_fig, style={'height': '80vh'}),
    dcc.Graph(id='disease-pie-chart'),
    dcc.Graph(id='disease-bar-chart')
])
