from flask import Flask 


def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty123'

    from .routes import route
    from .auth import auth

    app.register_blueprint(route, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app


