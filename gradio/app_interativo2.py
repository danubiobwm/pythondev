import gradio as gr
import string
from collections import Counter

def analisar_texto(texto):
    # Limpar o texto
    texto = texto.translate(str.maketrans("", "", string.punctuation)).lower()

    # Contar palavras
    palavras = texto.split()
    contagem_palavras = Counter(palavras)

    # Contar letras
    contagem_letras = Counter(texto.replace(" ", ""))

    # Contar frases
    contagem_frases = texto.count(".") + texto.count("!") + texto.count("?")

    # Criar o relatório
    relatorio = {
        "Número de palavras": len(palavras),
        "Número de letras": sum(contagem_letras.values()),
        "Número de frases": contagem_frases,
        "Contagem de palavras": dict(contagem_palavras),
        "Contagem de letras": dict(contagem_letras)
    }

    return relatorio

iface = gr.Interface(
    fn=analisar_texto,
    inputs=gr.Textbox(lines=10, label="Texto para Análise"),
    outputs="json",
    title="Analisador de Texto",
    description="Analise o texto inserido e obtenha informações sobre palavras, letras e frases.",
)
iface.launch()
