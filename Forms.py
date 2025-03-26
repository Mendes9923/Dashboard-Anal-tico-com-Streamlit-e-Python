import streamlit as st
import time as time
import datetime as datetime


def mostrarResultado():
    st.write("Cliente: ",varCliente)
    st.write("Banco: ", varBanco)
    st.write("Parcelas: ",varParcela)
    st.write("Data de Vencimento: ",varData)

with st.form('Formulario no Streamlit'):

    varModal = st.sidebar.selectbox(
        "Selecione o modal de transporte:",
        ("Rodoviário", "Marítimo", "Aéreo", "Trem", "Outro")
    )
    st.write("O modal selecionado foi :",varModal)

    with st.sidebar:
        varCliente = st.radio(
            "Selecione o cliente:",
            ("Space X", "Microsoft", "Apple", "Google", "Amazon")
        )
        varBanco = st.multiselect(
            "Selecione o banco:",
            ['Bradesco', 'Itaú', 'NU Bank', 'Caixa', 'Banco do Brasil']
        )
        varParcela = st.slider(
            "Quantas parcelas deseja financiar?", 0, 60, 30
        )
        varData = st.date_input(
            "Selecione a data do vencimento:",
            datetime.date(2025,1,1)
        )
        with st.spinner("Carregando....."):
            time.sleep(3)
        st.success("Pronto!")



    botao_form = st.form_submit_button("Filtrar")

    if botao_form:
        st.success("Obrigado por filtrar os dados")
        mostrarResultado()