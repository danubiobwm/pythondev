import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo = (
        f"background-color: {cor_fundo}; "
        f"color: {cor_texto}; "
        f"font-size: {tamanho_fonte}px; "
        f"font-family: {estilo_fonte}; "
        "padding: 10px; "
        "border-radius: 5px; "
    )
    return f"<div style='{estilo}'>{texto}</div>"

iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho da Fonte", value=20),
        gr.Dropdown(choices=["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"], label="Estilo da Fonte")
    ],
    outputs=gr.HTML(label="Texto Personalizado"),
    title="Personalizador de Texto",
    description="Customize o texto com cor de fundo, cor do texto, tamanho e estilo da fonte.",
)
iface.launch()