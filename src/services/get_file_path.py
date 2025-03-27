import tempfile
import os
from services.summary import summary


# Crio um diretorio temporario para salvar o arquivo e depois ler o arquivo
def file_path(file):
  if file is not None:
    temp_dir = tempfile.mkdtemp()
    path = os.path.join(temp_dir, file.name)
    with open(path, "wb") as f:
      f.write(file.getbuffer())
      # Chamo a função summary que realiza a leitura do arquivo e realiza o summario do texto usando o llama_index + Groq
      response = summary(path)
      return response
  return None
      