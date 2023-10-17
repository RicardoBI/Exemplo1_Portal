import streamlit as st
import pandas as pd
import plotly_express as px


@st.cache_data
def carregar_dados():
    dados = pd.read_excel('.\dados.xlsx', sheet_name='Resumos')
    return dados


st.set_page_config(
    page_title="Exemplo Com StreamLit para colunas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'Sobre': "# This is a header. This is an *extremely* _Aplicativo Legal!_"
    }
)

st.header(':bar_chart: Usando o Streamlit 🧊 ')
lateral = st.sidebar.header('Menu Principal')
escolhido = lateral.selectbox(
    "Escolha os dados", [
        'Gráfico de Linhas',
        'Gráfico de Barras',
        'Gráfico de Áreas',
        'Nenhum Gráfico'
    ], index=3
)


def gr_grafico(valor):
    valor = valor
    if escolhido == "Gráfico de Linhas":
        gr1 = st.line_chart(carregar_dados(), x=valor, y=str(
            'Valor_' + valor), color=(255, 0, 0), height=400)
    elif escolhido == "Gráfico de Barras":
        gr1 = st.bar_chart(carregar_dados(), x=valor, y=str(
            'Valor_' + valor), color=(0, 255, 0), height=400)
    elif escolhido == "Gráfico de Áreas":
        gr1 = st.area_chart(carregar_dados(), x=valor, y=str(
            'Valor_' + valor), color=(0, 0, 255), height=400)
    else:
        gr1 = ''
    return gr1


col1, col2 = st.columns(2)

with st.container():
    col1.markdown('#### Gráfico Estado')
    col2.markdown('#### Gráfico Lojas')
    with col1:
        gr_grafico('Estado')
    with col2:
        gr_grafico('Loja')

st.markdown('---')
st.markdown('#### Gráfico Cidades')
gr_grafico('Cidade')

dados2 = pd.read_excel('.\dados.xlsx', sheet_name='Unicos')
plot1 = px.line(dados2, x="Estado", y="Valor_Estado")
plot2 = px.bar(dados2, x="Estado", y="Valor_Estado")
plot3 = px.area(dados2, x="Estado", y="Valor_Estado")

st.plotly_chart(plot1)
col1.plotly_chart(plot2)
col2.plotly_chart(plot3)

tabela = st.sidebar.checkbox("Mostrar a tabela")
if tabela:
    with col2:
        dados2
