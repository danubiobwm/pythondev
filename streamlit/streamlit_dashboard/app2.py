import requests
import streamlit as st

# Configurações da página
st.set_page_config(page_title="Dashboard Streamlit")

# Título
st.title("Dashboard do Clima")

# Chave da API do OpenWeatherMap
api_key = "YOUR_API_KEY"

# URL da API do OpenWeatherMap para São Paulo
url = f"http://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo,BR&units=metric&appid={api_key}"

# Fazendo uma solicitação HTTP para a API do OpenWeatherMap
response = requests.get(url)

# Se a solicitação for bem-sucedida, exibe as informações do clima
if response.status_code == 200:
    data = response.json()
    st.write(f"Temperatura atual: {data['main']['temp']}°C")
    st.write(f"Umidade: {data['main']['humidity']}%")
    st.write(f"Condições: {data['weather'][0]['description']}")
else:
    st.write("Não foi possível obter as informações do clima.")
