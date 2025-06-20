import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Carregar dados
df = pd.read_csv("dados.csv")

# Título da página
st.title("Mapa de Calor - Cidade Segura")

# Selecionar categoria
categorias = ['assaltos', 'iluminacao', 'buracos', 'lixo', 'semaforos']
categoria = st.selectbox("Escolha a categoria:", categorias)

# Normalizar a coluna selecionada
df['valor'] = df[categoria] / df[categoria].max()

# Criar o mapa
latitude_central = df['lat'].mean()
longitude_central = df['lon'].mean()
mapa = folium.Map(location=[latitude_central, longitude_central], zoom_start=14)

# Adicionar camada de calor
heat_data = [[row['lat'], row['lon'], row['valor']] for _, row in df.iterrows()]
HeatMap(
    heat_data,
    radius=30,
    blur=20,
    max_opacity=0.5,
    min_opacity=0.2
).add_to(mapa)

# Exibir no Streamlit
st_folium(mapa, width=700, height=500)
