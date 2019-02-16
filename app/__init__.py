from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)
    db.init_app(app)

    # app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    # app.register_blueprint(main_blueprint)

    return app


