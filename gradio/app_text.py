import gradio as gr

def reverter_text(texto):
  texto_revertido = texto[::-1]
  return texto_revertido, len(texto_revertido)

#print(reverter_text("Olá, mundo!"))

iface = gr.Interface(
    fn=reverter_text,
    inputs=gr.Textbox(label="Texto de entrada"),
    outputs=[
        gr.Textbox(label="Texto revertido"),
        gr.Number(label="Número de caracteres")
    ],
    title="Reversor de Texto",
    description="Este aplicativo reverte o texto e conta o número de caracteres.",
    theme="default",
    allow_flagging="never"
)

iface.launch(share=True)

