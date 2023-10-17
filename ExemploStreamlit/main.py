import streamlit as st
import pandas as pd


@st.cache_data
def carregar_dados():
    dados = pd.read_excel('.\dados.xlsx', sheet_name='Resumos', header=None)
    return dados


def gr_estado():
    gr1 = st.bar_chart(carregar_dados(), x='Estado', y='Valor_Estado')
    return gr1


def gr_loja():
    gr2 = st.line_chart(carregar_dados(), x='Loja', y='Valor_Loja')
    return gr2


st.set_page_config(
    page_title="Exemplo com StreamLit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* Aplicativo Legal do BI!"
    }
)

st.header('Usando o Streamlit')
lateral = st.sidebar.markdown('## Barra Lateral de Menu')
gr_quant = st.sidebar.slider("Qtd de Gráficos", 0, 2, )

option = st.selectbox(
    'Estilo do Gráfico',
    ('Nenhum Gráfico', 'Barras do Estado', 'Linhas da Loja', 'Todos os Gráficos')
)

if gr_quant == 1:
    option = 'Barras de Estado'
elif gr_quant == 2:
    option = 'Todos os Gráficos'

botao = st.button('Todos os Gráficos')
if botao:
    option = 'Todos os Gráficos'

if option == 'Barras do Estado':
    gr_estado()
elif option == 'Linhas da Loja':
    gr_loja()
elif option == 'Todos os Gráficos':
    gr_estado()
    gr_loja()

texto = st.text_input("Seu nome", key="name")
st.session_state.name
st.write(texto)
