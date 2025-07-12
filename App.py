from flask import Flask
from extensions import db, mail, bcrypt
from Api.api import api
from Apps.main import main
from Apps.auth import auth
from Apps.crop import crop
from Apps.shop import shop
from Apps.query import query

def create_app():
    app = Flask(__name__)

    # Load config from environment variables with prefixes (FLASK_*)
    app.config.from_prefixed_env()

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(crop)
    app.register_blueprint(shop)
    app.register_blueprint(query)

    # Initialize REST API
    api.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
