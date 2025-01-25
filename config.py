#https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
import os
from dotenv import load_dotenv
load_dotenv() # importo arquivo .env que fica na raiz do projeto e configura as duas variáveis da classe Config

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") # CRiamos uma constante que pega das variáveis de ambiente o DATABASE_URI definido pelo desenvolvedor usando o comando export 
  SQLALCHEMY_TRACK_MODIFICATIONS = False
