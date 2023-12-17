from flask import Blueprint, request
from .controller import AuthController

auth_blueprint = Blueprint('auth', __name__)

controller_instance = AuthController()

@auth_blueprint.route('/login', methods=['POST'])
def loginRouter():
    data = request.get_json()
    res = controller_instance.login(data)
    return res