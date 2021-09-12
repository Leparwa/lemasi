from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

from flask_uploads import configure_uploads, IMAGES, UploadSet

photos = UploadSet('photos', IMAGES)
# Initializing app
def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['UPLOADED_PHOTOS_DEST'] = 'photos'
    configure_uploads(app, photos)

    # Initializing flask extensions
    bootstrap = Bootstrap(app)
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .main.requests import configure_request
    configure_request(app)
    
    return app