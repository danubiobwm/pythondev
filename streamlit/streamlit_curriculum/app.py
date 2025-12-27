from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais #
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "Curriculum.pdf"
arquivo_img = diretorio / "assets" / "foto.jpg"

# Configurações Geral das Informações #

TITULO = "Curriculum | Rodrigo Macedo"
NOME = "Rodrigo Macedo"
DESCRICAO = """
    Instrutor Cursos TI, com foco em Desenvolvimento Web e Data Science.
"""
EMAIL = "rcbm539@gmail.com"
MIDIA_SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/rodrigomacedodev/",
    "GitHub": "https://github.com/rcbmdev",
    "Youtube": "https://www.youtube.com/@rodrigodacostabarrosmacedo8475"
}

CURSOS = {
    "🎯 Desenvolvimento Web com o Flask": "https://www.udemy.com/course/desenvolvimento-web-com-flask/?referralCode=31CE040CA8B99CFEE224",
    "🎯 Assistente Virtual com Python": "https://www.udemy.com/course/assistente-virtual-com-python/?referralCode=49E270CD1BA677DC3D66",
    "🎯 Técnicas de Invasão com Kali Linux": "https://www.udemy.com/course/tecnicas-de-invasao-com-kali-linux/?referralCode=BA72D7277A683CC20F71",
    "🎯 Flutter com Flask": "https://www.udemy.com/course/flutter-com-flask-desenvolvendo-app-financas/?referralCode=1EB4C4A11C3F04D875F1",
    
}

st.set_page_config(
    page_title=TITULO
)

# Carregando Assets #

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem, width=250)
with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Download Curriculum",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write("✉️", EMAIL)

# Mídias Sociais #
st.write("#")
colunas = st.columns(len(MIDIA_SOCIAL))
for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].write(f"[{plataforma}]({link})")

# Experiências #
st.write("#")
st.subheader("Experiências")
st.write(
    """
        - 💹 7 anos de docência em disciplinas e cursos de Informática
        - 💹 Análise de Dados com Python e Power BI
        - 💹 Desenvolvimento Web com Flask e Django
    """
)

# Skills #
st.write("#")
st.subheader("Skills")
st.write(
    """
      - 📑 Programação (Python, Javascript)
      - 💹 Visualização de Dados: Power BI
      - 📖 NLP: NLTK e Spacy
      - 📷 VC: OpenCV   
    """
)

# Histórico de Trabalho #
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("---")

# Job 1 #
st.write("👨‍🏫", "**Professor Informática | Unibalsas**")
st.write("02/2017 - 10/2017")
st.write(
    """
        - 💹 Ministrando disciplinas voltadas à Engenharia de Software e Desenvolvimento de Software
    """
)

# Job 2 #
st.write("👨‍🏫", "**Professor Informática | IFMA**")
st.write("11/2017 - Atual")
st.write(
    """
        - 💹 Ministrando disciplinas como Sistemas Multimídas, Sistemas Operacionais, IHC, dentre outros.
        - 💹 Ministrando minicursos em temas focados em Data Science, como Chatbots, Análise de Dados, etc.
        
    """
)

# Cursos #
st.write("#")
st.subheader("Cursos")
st.write("---")
for curso, link in CURSOS.items():
    st.write(f"[{curso}]({link})")