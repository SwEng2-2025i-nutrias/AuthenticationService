from flask import Blueprint, request, jsonify
from flasgger import swag_from
from application.service.auth_service import AuthService
from adapters.output.unique_ider.uuid_ider import UUIDIder
from adapters.output.password_hasher.argon2_cffi_hasher import Argon2CffiHasher
from adapters.output.user_repository.local_db import LocalDBUserRepository
from adapters.output.jwt_handler.jwt_handler import JWTHandler

auth_blueprint = Blueprint('auth', __name__)

auth_service = AuthService(
    repo=LocalDBUserRepository(),
    hasher=Argon2CffiHasher(),
    unique_ider=UUIDIder(),
    token_handler=JWTHandler()
)

@auth_blueprint.route('/register', methods=['POST'])
@swag_from("docs/register_user.yaml")
def register_user():
    data = request.get_json()

    if data is None:
        return {"error": "Invalid or missing JSON body"}, 400

    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    role = data.get('role')

    if not email or not password or not name or not role:
        return jsonify({"error": "Missing required fields"}), 400

    try: 
        user = auth_service.register_user(email, password, name, role)
        return jsonify(user.public_to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@auth_blueprint.route('/login', methods=['POST'])
@swag_from("docs/login.yaml")
def login_user():
    data = request.get_json()

    if data is None:
        return {"error": "Invalid or missing JSON body"}, 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user = auth_service.login_user(email, password)
        token = auth_service.token_handler.generate_token(
            {"user_id": user.id, "email": user.email, "role": user.role}
        )
        data = {}
        data["user"] = user.public_to_dict()
        data["token"] = token
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

@auth_blueprint.route('/validate-token', methods=['GET'])
@swag_from("docs/validate_token.yaml")
def validate_token():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Missing Authorization header"}), 401
    
    if not token.startswith("Bearer "):
        return jsonify({"error": "Invalid Authorization header format"}), 401
    
    token = token.split(" ")[1]

    try:
        payload = auth_service.token_handler.verify_token(token)
        email = payload.get("email")
        if not email:
            return jsonify({"error": "Invalid token payload"}), 401
        
        user = auth_service.repo.get_user_by_email(email)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"valid": True, "user_id": user.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
