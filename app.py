# NOME:
# TURMA:
# laurindo.dumba@univille.br

# Importação das bibliotecas, para criar interfaces,
# realizar a manipulação dos dados e acesso ao modelo e geração de gráficos
import streamlit as st
import pandas as pd
import numpy as np
import os
from groq import Groq
import plotly.express as px


col1, col2 = st.columns([1, 5])

#with col1:
    #st.image("assets/Depeto.png", width=80)

st.markdown("""
    <h1 style='white-space: nowrap;'>
        DEPÊTO
    </h1>
""", unsafe_allow_html=True)



cls1, cls2, cls3 = st.columns(3)



with cls1:
    st.markdown(
        """
        <div style="background-color:#f0f0f0; padding:10px; border-radius:50px; color: black">
            <strong>Escreva alguma descrição </strong>
        </div>
        """,
        unsafe_allow_html=True
    )
    


with cls2:
    st.markdown(
        """
        <div style="background-color:#f0f0f0; padding:10px; border-radius:50px; color: black">
            <strong>Faça uma pergunta chave</strong>
        </div>
        """,
        unsafe_allow_html=True
    )
    


with cls3:
    st.markdown(
        """
        <div style="background-color:#f0f0f0; padding:10px; border-radius:50px; color: black">
            <strong>Cria outra pergunta </strong>
        </div>
        """,
        unsafe_allow_html=True
    )


GROQ_API_KEY = os.getenv("GROQ_API_KEY", "chave")

if not GROQ_API_KEY:
    st.error("A chave GROQ_API_KEY não foi definida corretamente!")
    st.stop()  
client = Groq(api_key=GROQ_API_KEY)


with st.sidebar:
    #st.image('assets/logo.png')
    uploaded_files = st.file_uploader(
        "Escolha o seu arquivo pdf", accept_multiple_files=True, type=["pdf"]
)


dataframes = {}

if uploaded_files:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        dataframes[uploaded_file.name] = df
        st.write(f"**{uploaded_file.name}**") 
        st.dataframe(df.head())
    
    
user_query = st.text_area("")


if st.button("Enviar Pergunta") and user_query:
    prompt = f"Responda como um analista de dados. Pergunta: {user_query}"
    response = client.chat.completions.create(model="llama3-8b-8192",
                                              messages=[{"role": "user", "content": prompt}])
    st.write("### Resposta do Agente:")
    st.write(response.choices[0].message.content)
    
    st.write("Resposta do Agente:")
    st.write(response.choices[0].message.content)
    



