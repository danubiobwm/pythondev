import streamlit as st
import pandas as pd
import collections
import plotly.express as px

# Importação / Manipulação Dados

def importa_dado():
    df = pd.read_csv("data/vgsales.csv")
    df = df.dropna()
    df = df[df['Year'] <= 2016]
    df['Year'] = df['Year'].astype(int)
    plataformas = ['Wii', 'PS2', 'PC', 'XOne', 'PS4']
    filtro = df['Platform'].isin(plataformas)
    return df[filtro]

df = importa_dado()

# Configuração Inicial #

st.set_page_config(page_title="📊Dashboard Games", layout="wide")

st.markdown("<h1 style='text-align: center;'>📊Dashboard Games</h1>",
            unsafe_allow_html=True)
st.markdown('---')

# Sidebar #

st.sidebar.header("Informe o Filtro Desejado:")
plataforma = st.sidebar.multiselect(
    "Selecione a plataforma",
    options=df["Platform"].unique(),
    default=df["Platform"].unique(),
)

genero = st.sidebar.multiselect(
    "Selecione o gênero",
    options=df["Genre"].unique(),
    default=df["Genre"].unique(),
)

df_selecao = df.query(
    "Platform == @plataforma & Genre == @genero"
)

# Frequência Vendas por Ano

freq_vendas = df_selecao.groupby('Year').count().sort_values('Name', ascending=False).reset_index()[['Year', 'Name']]
top_10 = freq_vendas.head(10)
grafico1 = px.bar(top_10, x='Year', y='Name', title="Frequência de Vendas",
                  labels={'Nome', 'Frequência'},
                  color_discrete_sequence=px.colors.sequential.Aggrnyl
                  )

# 10 jogos mais frequentes

top_10_freq_jogo = pd.DataFrame(collections.Counter(
    df_selecao['Name'].tolist()).most_common(10),
    columns=['Game', 'Frequency']
)

grafico2 = px.bar(top_10_freq_jogo, x='Game', y='Frequency')

coluna1, coluna2 = st.columns(2)
with coluna1:
    grafico1
with coluna2:
    grafico2

# Melhores Jogos

coluna = ['NA_Sales']
titulo = ['North America']

for i, c in enumerate(coluna):
    df_vendas = df_selecao.groupby('Name').sum().sort_values(c, ascending=False).head(10).reset_index()[['Name', c]]
    grafico3 = px.bar(df_vendas, x='Name', y=c,
                      title="Os 10 melhores jogos em {}".format(titulo[i]),
                      labels={'Name', 'Game'}
                      )
    grafico3












# Remove Estilo Streamlit
remove_st_estilo = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(remove_st_estilo, unsafe_allow_html=True)

