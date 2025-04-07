import gradio as gr

def converter_temperatura(temperatura, unidade):
    if unidade == "Celsius":
        return (temperatura * 9/5) + 32  # Celsius to Fahrenheit
    elif unidade == "Fahrenheit":
        return (temperatura - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Unidade inválida. Escolha Celsius ou Fahrenheit."

iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(minimum=-100, maximum=100, label="Temperatura"),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Unidade")
    ],
    outputs="number",
    title="Conversor de Temperatura",
    description="Converta temperaturas entre Celsius e Fahrenheit.",
)
iface.launch()