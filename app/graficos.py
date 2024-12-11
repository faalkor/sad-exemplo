import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def grafico(dados, idade_interesse):
    regioes = ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']

    # linha de interesse
    values =dados.loc[dados['Idade'] == idade_interesse, regioes].values[0]

    fig, ax = plt.subplots()
    ax.pie(values, labels=regioes, autopct='%1.1f%%', startangle=90)
    ax.axis('equal') 


    # Plotagem do grafico
    st.pyplot(fig)
