import streamlit as st
import pandas as pd
import requests

# Configurações da página
st.set_page_config(page_title="Dashboard COVID-19")

# Título
st.title("Dashboard COVID-19")

# API URL
url = "https://corona.lmao.ninja/v2/countries"

# Requisição GET
response = requests.get(url)

# Conversão em DataFrame
data = pd.DataFrame.from_dict(response.json())

# Filtrando as colunas necessárias
data = data[["country", "cases", "deaths", "recovered"]]

# Visualização dos dados
st.write("Dados de COVID-19:")
st.write(data)

# Gráficos
st.write("Gráficos:")
st.bar_chart(data.set_index("country"))
