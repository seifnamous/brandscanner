from flask import Flask
from routes import tweet
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.register_blueprint(tweet)
    return app

app = create_app(config_class=Config)
app.run(host = '0.0.0.0',port=4000, debug=True)
