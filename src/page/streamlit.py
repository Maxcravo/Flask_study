import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from io import StringIO
from src.services.get_file_path import file_path
import tempfile



st.title("Usando streamlit")

uploaded_file = st.file_uploader("Select a file", type="pdf")
if uploaded_file is not None:
  response = file_path(uploaded_file)
  if response is not None:
      # cria um arquivo temporario txt que armazena o texto do summario
      temp = tempfile.NamedTemporaryFile(suffix=".txt")
      temp.write(response.encode())
      temp.seek(0)
      with open(temp.name, "r+") as f:
        # Simplesmente o REACT nativo do python absolute cinema
        st.download_button(label="Download the summary", data=f)
        st.write(temp.name)