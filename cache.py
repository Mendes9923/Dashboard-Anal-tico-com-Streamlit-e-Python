import pandas as pd
import streamlit as st

@st.cache_data
def busca_df():
    df = pd.read_excel(
        io= './Datasets/faturamento.xlsx',
        engine='openpyxl',
        sheet_name='cache_teste',
        usecols='A:e',
        nrows=10000000,

    )
    return df

df =busca_df()

#sidebar
st.sidebar.header('MENU')
selecao_cliente = st.sidebar.multiselect(
    "Selecione o cliente",
    options=df["Cliente"].unique(),
    default=df["Cliente"].unique())
#Criar um novo df conforme o filtro do cliente
df_filtro_cliente = df.query(
  "Cliente == @selecao_cliente"
)

#adicionar ao sider bar a selecão de coluna aexibir
selecao_colunas =st.sidebar.multiselect(
    "Selecione a coluna á exibir",
    options=list(df_filtro_cliente),default=list(df_filtro_cliente))

df_printado = df_filtro_cliente.filter(items=selecao_colunas)


st.header('Como usar o *cache* no **Streamlit**')
df_printado
