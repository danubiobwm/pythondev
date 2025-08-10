from re import A
import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number

# Sample data for demonstration
st.set_page_config(page_icon=":bar_chart:", layout="wide")

st.title("Dashboard de Vendas 🛒")

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedor"])
with aba1:
    st.dataframe(df)

with aba2:
  coluna1, coluna2 = st.columns(2)
  with coluna1:
    st.metric("Receita Total", format_number(df['Preço'].sum(), 'R$'))
  with coluna2:
    st.metric("Quantidade Vendas", df.shape[0])

