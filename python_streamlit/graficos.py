from pdb import line_prefix
from turtle import title
import plotly.express as px
from utils import df_rec_estado, df_rec_mensal


grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat="lat",
    lon="lon",
    scope="south america",
    size= 'Preço',
    template="seaborn",
    hover_name = "Local da compra",
    hover_data = {"lat": False, "lon": False},
    title='Receita por Estado',
)


grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mes',
    y='Preço',
    markers=True,
    range_y=(0, df_rec_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal',

)

grafico_rec_mensal.update_layout(
    yaxis_title='Receita'
    )


grafico_rec_estado= px.bar(
    df_rec_estado.head(10),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top receita por Estado',

    )