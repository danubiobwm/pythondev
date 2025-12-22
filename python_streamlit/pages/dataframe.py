import streamlit as st
import pandas as pd


@st.cache_data
def load_data():

    from dataset import df

    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], dayfirst=True).dt.date
    return df

df = load_data()

st.title("Dataset de Vendas 🛒")

# 1. Seleção de Colunas
with st.expander("Colunas"):
    colunas = st.multiselect("Selecione as colunas", list(df.columns), list(df.columns))

# 2. Filtros na Sidebar
st.sidebar.title("Filtros")

with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect("Selecione a categoria",
                                df["Categoria do Produto"].unique(),
                                df["Categoria do Produto"].unique())

with st.sidebar.expander("Preço"):
    # O nome correto no seu JSON é "Preço"
    min_preco = float(df["Preço"].min())
    max_preco = float(df["Preço"].max())
    preco = st.slider("Selecione o preço", min_preco, max_preco, (min_preco, max_preco))

with st.sidebar.expander("Data da Compra"):
    data_compra = st.date_input("Selecione a data",
                                (df["Data da Compra"].min(), df["Data da Compra"].max()))

# 3. Lógica de Filtragem (Segura contra erros de seleção de data)
if len(data_compra) == 2:
    # Criando as máscaras de filtro
    mask_categoria = df["Categoria do Produto"].isin(categorias)
    mask_preco = (df["Preço"] >= preco[0]) & (df["Preço"] <= preco[1])
    mask_data = (df["Data da Compra"] >= data_compra[0]) & (df["Data da Compra"] <= data_compra[1])

    # Aplicando os filtros
    df_filtrado = df[mask_categoria & mask_preco & mask_data]

    # Exibindo o DataFrame
    st.dataframe(df_filtrado[colunas], use_container_width=True)

    # Resumo rápido abaixo da tabela
    st.markdown(f"**Total de registros encontrados:** {len(df_filtrado)}")
    st.markdown(f"**Soma total do valor filtrado:** R$ {df_filtrado['Preço'].sum():,.2f}")
else:
    st.info("Selecione o intervalo final de data para aplicar os filtros.")


# 4. Opção de Download
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode('utf-8')
csv_data = convert_df_to_csv(df_filtrado[colunas])
st.download_button(
    label="📥 Baixar dados filtrados em CSV",
    data=csv_data,
    file_name='dados_filtrados.csv',
    mime='text/csv',
)
