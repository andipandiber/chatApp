from flask import Flask

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO

app = Flask(__name__)

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()
csrf = CSRFProtect()




from .views import page
from .models import User


def create_app(config):
  app.config.from_object(config)

  bootstrap.init_app(app)
  csrf.init_app(app)


  socketio.init_app(app, message_queue=app.config['SOCKETIO_MESSAGE_QUEUE'])



  app.app_context().push()

  login_manager.init_app(app)
  login_manager.login_view = '.login_user'
  login_manager.login_message = 'Es Necesario Iniciar Sesion'

  app.register_blueprint(page)

  with app.app_context():
    db.init_app(app)
    db.create_all()

  return app
