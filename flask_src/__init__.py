from flask import Flask
from config import Config
from extensions import db
from flask_src.main import bp as main_bp
from flask_src.camera import bp as camera_bp
from flask_src.ai_integration import bp as ia_bp
from flask_src.db_controler import bp as db_bp
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv() # importo arquivo .env que fica na raiz do projeto e configura as duas variáveis da classe Config

def create_app(config_class=Config):
  app = Flask(__name__) # inicia uma instância do flask, para funcionar dessa forma é necessário definir a variavel de ambiente FLASK_APP=nome da pasta que fica o arquivo __init__.py
  app.config.from_object(config_class) # realiza o processo de configuracao da aplicacao envolvendo principalmente a conexão com o Banco de dados
  CORS(app) # habilita o CORS para todas as rotas da aplicacao
   
  # Initialize Flask extensions here
  db.init_app(app) # aqui iniciamos nosso db na nossa aplicacao

  # Register blueprints here
  app.register_blueprint(main_bp)
  app.register_blueprint(camera_bp)
  app.register_blueprint(ia_bp)
  app.register_blueprint(db_bp)
  
  
  @app.route("/test/")
  def test_page():
    return "<h1> The app is running </h1>"
  
  return app