# NOME:
# TURMA:
# laurindo.dumba@univille.br

# Importação das bibliotecas, para criar interfaces,
# realizar a manipulação dos dados e acesso ao modelo e geração de gráficos
import streamlit as st
import pandas as pd
import numpy as np
import pypdf
import os
from groq import Groq
import plotly.express as px


col1, col2 = st.columns([1, 5])


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
            <strong>Quais os documentos para admissão de servente? </strong>
        </div>
        """,
        unsafe_allow_html=True
    )
    


with cls2:
    st.markdown(
        """
        <div style="background-color:#f0f0f0; padding:10px; border-radius:50px; color: black">
            <strong>Tipos de afastamento no ponto eletrônico</strong>
        </div>
        """,
        unsafe_allow_html=True
    )
    


with cls3:
    st.markdown(
        """
        <div style="background-color:#f0f0f0; padding:10px; border-radius:50px; color: black">
            <strong>Como funciona o pagamento do prêmio frequência? </strong>
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
    uploaded_files = st.file_uploader(
        "Escolha o seu arquivo pdf", accept_multiple_files=True, type=["pdf"]
)

dataframes = {}

uploaded_file = st.file_uploader("Envie um arquivo", type=["csv", "pdf"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    elif file_type == "pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        st.text_area("Conteúdo extraído do PDF:", text, height=300)

    else:
        st.warning("Tipo de arquivo não suportado.")
    
    
user_query = st.text_area("")


if st.button("Enviar Pergunta") and user_query:
    prompt = f"Responda como um analista de dados. Pergunta: {user_query}"
    response = client.chat.completions.create(model="llama3-8b-8192",
                                              messages=[{"role": "user", "content": prompt}])
    st.write("### Resposta do Agente:")
    st.write(response.choices[0].message.content)
    
    st.write("Resposta do Agente:")
    st.write(response.choices[0].message.content)
    








