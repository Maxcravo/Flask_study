#https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  try:
    SQLALCHEMY_URI = os.environ.get("DATABASE_URI")
  except: 
    print ("CONFIGURAR O DATABSE URI nas variáveis de ambiente")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
    