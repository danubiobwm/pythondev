import gradio as gr
import math

def fatorial(n):
    if n < 0:
        return "Fatorial não existe para números negativos"
    return math.factorial(n)

#print("Fatorial de 5:", fatorial(5))  # Exemplo de uso

iface = gr.Interface(
    fn=fatorial,
    inputs=gr.Number(label="Enter a number"),
    outputs="text",
    title="Calculadora de Fatorial",
    description="Esta aplicação calcula o fatorial de um número inteiro não negativo.",
    theme="default",
)

iface.launch()