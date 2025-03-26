import streamlit as st
import time

myBar = st.progress(0)
for num in range(100):
    time.sleep(0.03)
    myBar.progress(num+1)

with st.spinner("Aguarde..."):
    time.sleep(1)
st.success('Seu dateset foi carregado com sucesso.')
st.error('Caracter invalido')
st.warning('Data fora do intervalo padrão.')    
st.info('Os resultados já foram carregados na base.')

e = RuntimeError('Exceção do tipo RuntimeRrror.')
st.exception(e)


#animaçoes 

st.snow()
st.balloons()