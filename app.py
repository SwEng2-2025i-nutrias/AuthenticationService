from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from adapters.input.auth.auth_controller import auth_blueprint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(override=True)

app = Flask(__name__)
CORS(app, resources={r"/auth/*": {
    "origins": ["*"],
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})

# Initialize Swagger for API documentation
swagger = Swagger(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=5001)