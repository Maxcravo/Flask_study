import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from io import StringIO
from src.services.get_file_path import file_path
from src.services.summary import test_gemini
import tempfile
import re

st.title("Resumo e Diagrama do texto")
uploaded_file = st.file_uploader("Select a file", type="pdf")
if uploaded_file is not None:
  response = file_path(uploaded_file)
  if response is not None:
      # cria um arquivo temporario txt que armazena o texto do summario
      temp = tempfile.NamedTemporaryFile(suffix=".txt")
      # Usamos um regex para remover o texto que está entre o <think> e </think>(.*?)
      response = clean_text = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
      temp.write(response.encode())
      temp.seek(0)
      with open(temp.name, "r+") as f:
        # Simplesmente o REACT nativo do python absolute cinema
        st.download_button(label="Download the summary", data=f, file_name="summary.txt")
        st.write(temp.name)

st.button("Test Gemini", on_click=test_gemini)

