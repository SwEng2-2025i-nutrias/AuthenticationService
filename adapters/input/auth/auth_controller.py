from flask import Blueprint, request, jsonify
from flasgger import swag_from
from application.service.auth_service import AuthService
from adapters.output.unique_ider.uuid_ider import UUIDIder
from adapters.output.password_hasher.argon2_cffi_hasher import Argon2CffiHasher
from adapters.output.user_repository.local_db import LocalDBUserRepository

auth_blueprint = Blueprint('auth', __name__)

auth_service = AuthService(
    repo=LocalDBUserRepository(),
    hasher=Argon2CffiHasher(),
    unique_ider=UUIDIder()
)

@auth_blueprint.route('/register', methods=['POST'])
@swag_from()
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
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@auth_blueprint.route('/login', methods=['POST'])
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
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
