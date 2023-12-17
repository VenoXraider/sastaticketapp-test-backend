from flask import Blueprint
from .auth import auth_blueprint
from .sheets import sheets_blueprint

v1_blueprint = Blueprint('v1', __name__)

v1_blueprint.register_blueprint(auth_blueprint, url_prefix='/auth')
v1_blueprint.register_blueprint(sheets_blueprint, url_prefix='/sheets')