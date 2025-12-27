import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

st.title('Storytelling Data App')

def cria_grafico():
    chart = Chart(width="600px", height="300px", display="manual")
    data = Data()
    dataframe = pd.read_csv("data/titanic.csv")
    data.add_data_frame(dataframe)
    chart.animate(data)

    # configurações #

    chart.animate(
        Config(
            {
                "x":"Count", "y": "Sex",
                "label":"Count",
                "title": "Passageiros do Titanic"
            }
        )
    )

    chart.animate(
        Config(
            {
                "x":["Count", "Survived"],
                "label":["Count", "Survived"],
                "color": "Survived"
            }
        )
    )

    chart.animate(
        Config(
            {
                "x": "Count",
                "y":["Sex", "Survived"]
            }
        )
    )

    # Style #
    chart.animate(
        Style(
            {
                "title": {"fontSize": 35}
            }
        )
    )

    return chart._repr_html_()

GRAFICO = cria_grafico()
html(GRAFICO, width=600, height=300)