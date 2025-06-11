from flask import Flask
from flasgger import Swagger
from adapters.input.auth.auth_controller import auth_blueprint

app = Flask(__name__)

# Initialize Swagger for API documentation
swagger = Swagger(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=5001)