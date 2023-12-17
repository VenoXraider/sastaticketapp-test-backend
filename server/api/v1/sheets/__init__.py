from flask import Blueprint, request
from .controller import AuthController

sheets_blueprint = Blueprint('sheets', __name__)

controller_instance = AuthController()

@sheets_blueprint.route('/', methods=['POST'])
def getSheetsRouter():
    data = request.get_json()
    res = controller_instance.getSheetsRouter(data)
    return res

@sheets_blueprint.route('/send/email', methods=['POST'])
def getSheetsRouter():
    data = request.get_json()
    res = controller_instance.sendEmail(data)
    return res