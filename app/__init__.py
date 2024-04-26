from flask import Flask
from flask_socketio import SocketIO

def create_app():
    app = Flask(__name__)
    socketio = SocketIO(app)
    from .routes import main
    app.register_blueprint(main)
    return app, socketio
