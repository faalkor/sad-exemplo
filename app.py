import streamlit as st
import folium
import json
import pandas as pd
from graficos import grafico


# cabecalho
st.markdown("# Pessoas com celular Brasil 2005")


# Mapa
with open('paises.json') as f:
    paisesJson = json.load(f)
    m = folium.Map(location=[20, 0], zoom_start=2)
    folium.GeoJson(
        paisesJson,
        style_function=lambda x: {
            'fillColor': 'green',
            'fillOpacity': 1
        }
        if x['properties']['name'] == 'Brazil' else{}).add_to(m)
    
    st.components.v1.html(m._repr_html_(), height=450)


# Tabela
st.markdown("## Dados")
df = pd.read_csv('dataset.csv')
st.write(df)


# Graficos
st.markdown("### 20 a 24 anos")
grafico(df, "20_a_24")

st.markdown("### 60+ anos")
grafico(df, "60_+")
