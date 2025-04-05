import gradio as gr
import numpy as np
from PIL import Image
import io
import base64

def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
  estilo = (
    f"background-color: {cor_fundo}; "
    f"color: {cor_texto}; "
    "padding: 20px; "
    "text-align: center; "
  )

  # Convert the image to base64
  imagem_html=""
  if imagem is not None:
    buffer = io.BytesIO()
    Image.fromarray(imagem).save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    imagem_html=(
      f"<img src='data:image/png;base64,{img_str}'"
      " style='max-width: 100%; height: auto;' />"
    )

  slide_html = f"""
  <div style="{estilo}">
    <h1>{titulo}</h1>
    <p>{texto}</p>
    {imagem_html}
  </div>
  """

  return slide_html

iface = gr.Interface(
  fn=criar_slide,
  inputs=[
    gr.Textbox(label="Título"),
    gr.Textbox(label="Texto"),
    gr.Image(type="numpy", label="Imagem"),
    gr.ColorPicker(label="Cor de Fundo"),
    gr.ColorPicker(label="Cor do Texto")
  ],
  outputs=gr.HTML(label="Slide HTML"),
  title="Gerador de Slides",
  description="Crie um slide HTML com título, texto, imagem e cores personalizadas."
)
iface.launch(share=True)