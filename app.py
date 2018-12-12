from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    # app.config.from_envvar('APPLICATION_SETTINGS')
    
    from api import api_bp
    app.register_blueprint(api_bp)

    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__": # pragma: no cover
    app = create_app("config")
    app.run(debug=True)

