from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config.DevelopmentConfig)

  
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(db)


    return app