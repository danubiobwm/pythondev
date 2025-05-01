import streamlit as st # type: ignore
import dados

st.title("Form Filmes")
nome = st.text_input("Nome do filme:")
ano = st.number_input("Ano do filme:", min_value=1900, max_value=2100, step=1)
nota = st.slider("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button("Adicionar"):
    # Conectando ao banco de dados
    conexao = dados.connect_db()

    # Inserindo os dados no banco de dados
    dados.insert_data(conexao, nome, ano, nota)

    st.success("Dados inseridos com sucesso!")


# Listando os dados do banco de dados
conexao = dados.connect_db()
resultado = dados.list_data(conexao)
st.subheader("Lista de Filmes")
for filme in resultado:
    st.write(f"Nome: {filme[1]}, Ano: {filme[2]}, Nota: {filme[3]}")